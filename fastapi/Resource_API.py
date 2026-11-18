from fastapi import FastAPI, HTTPException

app = FastAPI()

lab_equipment_db = [
    {
        "id": "multimeter-01",
        "item_name": "Digital Multimeter",
        "category": "Testing & Measurement",
        "total_stock": 15,
        "available_stock": 12,
        "location": "Lab 304 - Electronics Wing",
        "is_active": True
    },
    {
        "id": "arduino-mega-05",
        "item_name": "Arduino Mega 2560",
        "category": "Microcontrollers",
        "total_stock": 10,
        "available_stock": 4,
        "location": "Lab 302 - Embedded Systems",
        "is_active": True
    },
    {
        "id": "soldering-station-02",
        "item_name": "Temperature-Controlled Soldering Station",
        "category": "Hardware Tools",
        "total_stock": 8,
        "available_stock": 0,
        "location": "Lab 304 - Electronics Wing",
        "is_active": False
    }
]

@app.get("/equipment")
def get_all_equipment():
    return lab_equipment_db

@app.get("/equipment/{item_id}")
def get_equipment_by_id(item_id: str):
    for item in lab_equipment_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="The equipment item doesn't exist in the database.")

@app.post("/equipment/new")
def add_new_equipment(new_item: dict):
    lab_equipment_db.append(new_item)
    return {"message": "New lab equipment registered successfully."}

@app.patch("/equipment/{item_id}")
def update_equipment_data(item_id: str, updated_data: dict):
    for index, item in enumerate(lab_equipment_db):
        if item["id"] == item_id:
            lab_equipment_db[index].update(updated_data)
            return {"message": "Equipment data updated successfully."}
    raise HTTPException(status_code=404, detail="The equipment item doesn't exist in the database.")

@app.put("/equipment/{item_id}")
def replace_equipment(item_id: str, replacement_item: dict):
    for index, item in enumerate(lab_equipment_db):
        if item["id"] == item_id:
            lab_equipment_db[index] = replacement_item
            return {"message": "Equipment record replaced successfully."}
    raise HTTPException(status_code=404, detail="The equipment item doesn't exist in the database.")

@app.delete("/equipment/{item_id}")
def delete_equipment(item_id: str):
    for index, item in enumerate(lab_equipment_db):
        if item["id"] == item_id:
            del lab_equipment_db[index]
            return {"message": "Equipment record removed successfully."}
    raise HTTPException(status_code=404, detail="The equipment item doesn't exist in the database.")