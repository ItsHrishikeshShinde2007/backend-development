from fastapi import FastAPI
from src.routers import hello, cars

app = FastAPI()

app.include_router(hello.router)
app.include_router(cars.router)

@app.get("/")
def root():
    return {"message": "Backend Development API is running."}
