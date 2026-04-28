from pydantic import BaseModel

class Addition(BaseModel):
    additional_info: str
    additional_number: int

class Entity(BaseModel):
    id: int
    addition: Addition
    important_numbers: list[int]
    title: str
    verified: bool