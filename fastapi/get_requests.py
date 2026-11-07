Drivers = [
    {
        "Driver Name":"Kimi Antonelli",
        "Car_No":"12",
        "Team":"Mercedes",
        "Points":"380"
    },
    {
        "Driver Name":"Max Verstappen",
        "Car_No":"3",
        "Team":"Red Bull Racing",
        "Points":"261"
    },
    {
        "Driver Name":"Lewis Hamilton",
        "Car_No":"44",
        "Team":"Scuderia Ferrari",
        "Points":"259"
    }
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/drivers")
def all_drivers():
    return Drivers

@app.get("/drivers/{Points}")
def driver(Points: str):
    for drivers in Drivers:
        if drivers["Points"] == Points:
            return drivers
    return {"error": "Driver not found"}