from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5000",
        "http://127.0.0.1:5000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "database/backend.db"

def get_db():
    connection = sqlite3.connect(DATABASE_URL)
    connection.row_factory = sqlite3.Row ##This just simply converts each database row into a dictionary-like object, allowing you to access columns by name instead of index.

    try:
        yield connection ##and this as it suggests, provides the connection to the endpoint
    finally:
        connection.close() ##ensures thatt the connection is closed after the request

@app.get("/cars")
def get_cars(connection: sqlite3.Connection = Depends(get_db)): ## tells FastAPI to obtain the connection through our dependency.
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cars;")
    
    cars = cursor.fetchall()
    return [dict(car) for car in cars]
    ## This basically retrieves all cars from the database and prints them

@app.get("/cars/{car_id}")
def get_car(car_id: int, connection: sqlite3.Connection = Depends(get_db)):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cars WHERE car_id = ?;", (car_id,))
    
    car = cursor.fetchone()
    if car is not None:
        return dict(car)
    else:
        return {"Message": "Car not found."}

@app.post("/cars/new/{car_id}")
def add_new_car(car: dict, connection: sqlite3.Connection = Depends(get_db)):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO cars (car_id, name, company, type, manufacturing_year, horsepower) VALUES (?, ?, ?, ?, ?, ?);",
        (car["car_id"], car["name"], car["company"], car["type"], car["manufacturing_year"], car["horsepower"])
    )
    connection.commit()
    return {"message": "New car added successfully.", "car": car}

@app.put("/cars/new/{car_id}")
def update_car(car_id: int, updated_car: dict, connection: sqlite3.Connection = Depends(get_db)):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE cars SET name = ?, company = ?, type = ?, manufacturing_year = ?, horsepower = ? WHERE car_id = ?;",
        (updated_car["name"], updated_car["company"], updated_car["type"], updated_car["manufacturing_year"], updated_car["horsepower"], car_id)
    )
    connection.commit()
    return {"message": "Car updated successfully.", "updated_car": updated_car}