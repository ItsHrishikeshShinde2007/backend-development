Cars = [
    {
        "Company": "Koenigsegg",
        "Model": "Jesko Absolut",
        "Horse power": "1,200 hp",
    },
    {
        "Company": "Biggati",
        "Model": "La Voiture Noire",
        "Horse power": "1,479 hp",
    },
    {
        "Company": "Hennessey Special Vehicles",
        "Model": "Venom F5",
        "Horse power": "1,817 hp",
    }
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/main")
def get_fastest_cars():
    return {
        "message": "This is the list of all fastest cars in the world",
        "list": Cars
    }