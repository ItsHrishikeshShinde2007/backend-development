drivers = [
    {"name":"Max", 
     "number":1},
    {"name":"Charles", 
     "number":16},
    {"name":"Fernando", 
     "number":14}
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/drivers")
def get_drivers():
    return drivers

@app.get("/drivers/{number}")
def get_driver_by_number(number: int):
    for driver in drivers:
        if driver["number"] == number:
            return driver
    return {"error": "Driver not found"}