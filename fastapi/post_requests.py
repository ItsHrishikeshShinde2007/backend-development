drivers = [
    {"name":"Max", 
     "number":1},
    {"name":"Charles", 
     "number":16},
    {"name":"Fernando", 
     "number":14}
]

newdriver = {
    "name": "New Driver", 
    "number": 0
}

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

def addnewdriver(newdriver):
    input_name = input("Enter the name of the new driver: ")
    input_number = int(input("Enter the number of the new driver: "))
    input_index = int(input("Enter the index where you want to add the new driver: "))
    if(input_index == 0):
        print("Lol you wish if that happened but it won't happen because Max verstappen is the best driver in the world and he will always be number 1")
    else:
        newdriver = {"name": input_name, "number": input_number}
        drivers.insert(input_index, newdriver)
        return {"message": "New driver added successfully."}

@app.post("/addnewdriver")
def add_new_driver():
    return addnewdriver(newdriver)