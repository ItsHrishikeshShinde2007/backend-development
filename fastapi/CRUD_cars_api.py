import sqlite3
from fastapi import FastAPI, Depends

app = FastAPI()

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