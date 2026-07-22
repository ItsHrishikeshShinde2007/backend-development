drivers = [
    {
        "Name" : "Max Verstappen",
        "Team" : "Red Bull racing",
        "Number" : 1
    },
    {
        "Name" : "Sebastian Vettel",
        "Team" : "Red Bull racing",
        "Number" : 1
    },
    {
        "Name" : "Fernando Alonso",
        "Team" : "Scuderia Ferrari",
        "Number" : 1
    }
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_drivers():
    return {
        "message": "This is the list of all GOATS of F1",
        "list": drivers
    }

champion_candidates = [
    {
        "name": "Lance Stroll",
        "team": "Aston Martin Formula One team",
        "number": 1
    },
    {
        "name": "Estaban Ocon",
        "team": "Haas Forula 1 team",
        "number": 1
    },
    {
        "name": "Oliever bearman",
        "team": "Scuderia Ferrari",
        "number": 1
    }
]

@app.get("/champions")
def get_champions():
    return {
        "message": "These are the drivers who also have the potential to become a Champion",
        "unique_list": champion_candidates
    }