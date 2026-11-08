import sqlite3
from fastapi import APIRouter, Depends

from database.connection import get_db

router = APIRouter()

@router.get("/cars")
def get_cars(connection: sqlite3.Connection = Depends(get_db)):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cars;")

    cars = cursor.fetchall()

    return [dict(car) for car in cars]

@router.get("/cars/{car_id}")
def get_car(car_id: int, connection: sqlite3.Connection = Depends(get_db)):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cars WHERE car_id = ?;", (car_id,))

    car = cursor.fetchone()

    if car is not None:
        return dict(car)

    return {"message": "Car not found."}