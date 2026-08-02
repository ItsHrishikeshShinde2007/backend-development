laptops = [
    {
        "Brand": "Lenovo",
        "Model": "Legion Pro 7i",
        "CPU": "Intel Core Ultra 9 275HX",
        "GPU": "NVIDIA RTX NVIDIA GeForce RTX 5070 Ti (12GB GDDR7)",
        "Price": 359991
    },
    {
        "Brand": "Asus",
        "Model": "ROG Strix SCAR 16",
        "CPU": "Intel Core Ultra 9 275HX",
        "GPU": "NVIDIA RTX NVIDIA GeForce RTX 5090 (24GB GDDR7)",
        "Price": 449990
    },
    {
        "Brand": "Dell",
        "Model": "Alienware M18 R2",
        "CPU": "Intel Core i9-14900HX",
        "GPU": "NVIDIA RTX NVIDIA GeForce RTX 4090 (16GB GDDR6)",
        "Price": 513121
    }
]

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Laptop(BaseModel):
    Brand: str
    Model: str
    CPU: str
    GPU: str
    Price: int

@app.get("/Laptops")
def get_laptops():
    return laptops

@app.post("/Laptops")
def add_new_laptop(laptop: Laptop):
    new_laptop = laptop.model_dump()
    laptops.append(new_laptop)

    return{
        "message": "New laptop added successfully.",
        "laptop": new_laptop
    }