Mods = [
    {
        "Mod Name":"Twin Screw Supercharger",
        "Mod Type":"Forced Induction",
        "Mod Price":550000,
        "Increase in HP":180,
        "Increase in Top Speed":28
    },
    {
        "Mod Name":"Performance Racing Headers",
        "Mod Type":"Exhaust System",
        "Mod Price":120000,
        "Increase in HP":25,
        "Increase in Top Speed":5
    },
    {
        "Mod Name":"Forged Crankshafts",
        "Mod Type":"valvetrain",
        "Mod Price":180000,
        "Increase in HP":35,
        "Increase in Top Speed":6
    },
    {
        "Mod Name":"Performance Intake Manifold",
        "Mod Type":"Air Intake",
        "Mod Price":110000,
        "Increase in HP":18,
        "Increase in Top Speed":3
    },
    {
        "Mod Name":"Roots Supercharger Upgrade",
        "Mod Type":"Forced Induction",
        "Mod Price":380000,
        "Increase in HP":160,
        "Increase in Top Speed":24
    },
    {
        "Mod Name":"Performance Camshaft",
        "Mod Type":"Valvetrain",
        "Mod Price":110000,
        "Increase in HP":35,
        "Increase in Top Speed":5
    }
]

from fastapi import FastAPI

app = FastAPI()

@app.get("/mods")
def getallmods():
    return Mods

@app.post("/mods")
def addanewmod(mod : dict):
    Mods.append(mod)
    return {"New Mod added Successfully":"Mod"}