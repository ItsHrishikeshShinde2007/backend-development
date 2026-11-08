Cars = [
    {
        "Car_ID": 1,
        "Make": "Bugatti",
        "Model": "Chiron Super Sport",
        "Top_Speed_MPH": 304.7,
        "Zero_To_Sixty_Secs": 2.2,
        "Production_Run": 30,
        "Is_Electric": False
    },
    {
        "Car_ID": 2,
        "Make": "Koenigsegg",
        "Model": "Jesko Absolut",
        "Top_Speed_MPH": 330.0,
        "Zero_To_Sixty_Secs": 2.5,
        "Production_Run": 125,
        "Is_Electric": False
    },
    {
        "Car_ID": 3,
        "Make": "Rimac",
        "Model": "Nevera",
        "Top_Speed_MPH": 258.0,
        "Zero_To_Sixty_Secs": 1.74,
        "Production_Run": 150,
        "Is_Electric": True
    },
    {
        "Car_ID": 4,
        "Make": "Pagani",
        "Model": "Huayra Roadster BC",
        "Top_Speed_MPH": 238.0,
        "Zero_To_Sixty_Secs": 2.9,
        "Production_Run": 40,
        "Is_Electric": False
    },
    {
        "Car_ID": 5,
        "Make": "Porsche",
        "Model": "Mission X",
        "Top_Speed_MPH": 250.0,
        "Zero_To_Sixty_Secs": 1.9,
        "Production_Run": 200,
        "Is_Electric": True
    }
]

from fastapi import FastAPI, HTTPException

myapp = FastAPI()

@myapp.get("/cars")
def get_all_the_cars():
    return Cars

@myapp.delete("/cars/{Car_ID}")
def delete_a_car(Car_ID:int):
    for car in Cars:
        if car["Car_ID"] == Car_ID:
            Cars.remove(car)
            return{"Message":"car has successfully deleted","Deleted Car":car}
    raise HTTPException(status_code=404, detail={"Warning":"the car that you are trying to delete does not exist in the database","Quick Fix":"Try seeing the car's ID from the /cars endpoints and try again"})
