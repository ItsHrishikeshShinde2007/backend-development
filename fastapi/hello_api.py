from fastapi import FastAPI

app = FastAPI()

@app.get("/Hellothere")
def hello():
    return{"Hello there how are you doing today?"}