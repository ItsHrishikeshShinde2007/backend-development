from pydantic import BaseModel

class Car(BaseModel):
    name: str
    company: str
    type: str
    manufacturing_year: int
    horsepower: int
