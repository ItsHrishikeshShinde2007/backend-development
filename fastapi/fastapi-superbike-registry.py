superbikes_db = [
    {
        "id": "ducati-panigale-v4",
        "brand": "Ducati",
        "model": "Panigale V4 S",
        "year": 2025,
        "engine": {
            "displacement_cc": 1103,
            "type": "90-degree V4",
            "horsepower_bhp": 216,
            "torque_nm": 120.9
        },
        "top_speed_kmh": 299,
        "wet_weight_kg": 187,
        "electronics": ["Cornering ABS", "Ducati Traction Control", "Wheelie Control", "Bi-directional Quickshifter"],
        "is_street_legal": True,
        "price_inr_lakhs": 33.48
    },
    {
        "id": "bmw-s1000rr",
        "brand": "BMW",
        "model": "S 1000 RR M Package",
        "year": 2025,
        "engine": {
            "displacement_cc": 999,
            "type": "Inline-4 ShiftCam",
            "horsepower_bhp": 210,
            "torque_nm": 113.0
        },
        "top_speed_kmh": 303,
        "wet_weight_kg": 193.5,
        "electronics": ["Dynamic Traction Control", "Slide Control", "Launch Control", "Pit Lane Limiter"],
        "is_street_legal": True,
        "price_inr_lakhs": 25.25
    },
    {
        "id": "kawasaki-zx10r",
        "brand": "Kawasaki",
        "model": "Ninja ZX-10R",
        "year": 2025,
        "engine": {
            "displacement_cc": 998,
            "type": "Inline-4",
            "horsepower_bhp": 203,
            "torque_nm": 114.9
        },
        "top_speed_kmh": 299,
        "wet_weight_kg": 207,
        "electronics": ["KCMF Cornering Management", "Sport-Kawasaki Traction Control", "Electronic Cruise Control"],
        "is_street_legal": True,
        "price_inr_lakhs": 17.93
    },
    {
        "id": "yamaha-r1",
        "brand": "Yamaha",
        "model": "YZF-R1M",
        "year": 2025,
        "engine": {
            "displacement_cc": 998,
            "type": "Crossplane Inline-4",
            "horsepower_bhp": 200,
            "torque_nm": 113.3
        },
        "top_speed_kmh": 299,
        "wet_weight_kg": 202,
        "electronics": ["6-Axis IMU", "Ohlins Electronic Racing Suspension", "Brake Control System"],
        "is_street_legal": True,
        "price_inr_lakhs": 29.50
    }
]

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/superbikes")
def getalbikes():
    return superbikes_db

@app.get("/superbikes/{bike_id}")
def getonlythisbike (bike_id: str):
    for bike in superbikes_db:
        if bike["id"] == bike_id:
            return bike
    raise HTTPException(status_code = 404, detail = "The bike doesn't exist in the database.")

@app.post("/superbikes/new")
def getnewbike(new_bike: dict):
    superbikes_db.append(new_bike)
    return {"Message":"The new bike is added successfully."}

@app.patch("/superbikes/{bike_id}")
def updatebikedata(bike_id: str, updated_bike: dict):
    for index, bike in enumerate(superbikes_db):
        if bike["id"] == bike_id:
            superbikes_db[index].update(updated_bike)
            return{"message":"The bike data is updated at index successfully."}
    raise HTTPException(status_code = 404, detail = "The bike doesn't exist in the database.")

@app.put("/superbikes/{bike_id}")
def updatebike(bike_id: str, updated_bike: dict):
    for index, bike in enumerate(superbikes_db):
        if bike["id"]== bike_id:
            superbikes_db[index] = updated_bike
            return{"message":"The bike is updated at index successfully."}
    raise HTTPException(status_code = 404, detail = "The bike doesn't exist in the database.")

@app.delete("/superbikes/{bike_id}")
def deletebike(bike_id: str):
    for index, bike in enumerate(superbikes_db):
        if bike["id"] == bike_id:
            del superbikes_db[index]
            return {"message":"The superbike is deleted successfully."}
    raise HTTPException(status_code = 404, detail = "The bike doesn't exist in the database.")