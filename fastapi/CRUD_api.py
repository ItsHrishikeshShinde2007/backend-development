gpus = [
    {
        "ID": 1,
        "Brand": "MSI",
        "Model": "Ventus 3X OC",
        "GPU": "RTX 5080",
        "VRAM": "16 GB GDDR7",
        "Price": 164500
    },
    {
        "ID": 2,
        "Brand": "GIGABYTE",
        "Model": "Gaming OC",
        "GPU": "RTX 5070 Ti",
        "VRAM": "16 GB GDDR7",
        "Price": 132999
    },
    {
        "ID": 3,
        "Brand": "Sapphire Technology",
        "Model": "NITRO+ Vapor-X OC",
        "GPU": "RX 7900 XTX",
        "VRAM": "24 GB GDDR6",
        "Price": 107900
    },
    {
        "ID": 4,
        "Brand": "ZOTAC",
        "Model": "Twin Edge OC",
        "GPU": "RTX 5070",
        "VRAM": "12GB GDDR7",
        "Price": 76500
    },
    {
        "ID": 5,
        "Brand": "ASUS",
        "Model": "Prime OC Edition",
        "GPU": "RTX 5060 Ti",
        "VRAM": "16GB GDDR7",
        "Price": 85500
    },
]

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GPU(BaseModel):
    ID: int
    Brand: str
    Model: str
    GPU: str
    VRAM: str
    Price: int

@app.get("/gpus")
def get_gpus():
    return gpus

@app.post("/gpus")
def add_new_gpu(gpu: GPU):
    new_gpu = gpu.model_dump()
    gpus.append(new_gpu)

    return{
        "message": "New GPU added successfully.",
        "gpu": new_gpu
    }

@app.get("/gpus/{ID}")
def get_gpu(ID: int):
    for gpu in gpus:
        if gpu["ID"] == ID:
            return gpu
    return {"Message":"Not found the GPU with the given ID."}

@app.put("/gpus/{ID}")
def update_gpu(ID: int, new_gpu: GPU):
    for index, gpu in enumerate(gpus):
        if gpu["ID"] == ID:
            gpus[index] = new_gpu.model_dump()
            return{
                "message":"Gpus updates successfully.",
                "Updated gpus": new_gpu.model_dump()
            }
    return {"Message":"Gpu not found."}

@app.patch("/gpus/{ID}")
def update_gpu_price(ID: int, new_gpu: GPU):
    for index, gpu in enumerate(gpus):
        if gpu["ID"] == ID:
            gpus[index]["Price"] = new_gpu.Price
            return{
                "message":"Gpu price updated successfully.",
                "Updated gpus": gpus[index]
            }
    return {"Message":"Gpu not found."}

@app.delete("/gpus/{ID}")
def delete_gpu(ID: int):
    for index, gpu in enumerate(gpus):
        if gpu["ID"] == ID:
            deleted_gpu = gpus.pop(index)
            return{
                "message":"Gpu deleted successfully.",
                "Deleted gpus": deleted_gpu
            }
    return {"Message":"Gpu not found."}