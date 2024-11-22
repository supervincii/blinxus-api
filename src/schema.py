from pydantic import BaseModel
import uuid
from datetime import date

class User(BaseModel):
    id: uuid.UUID
    name: str
    birthday: date
    nationality: str
    interests: list[str] | None

class Favorites(BaseModel):
    food: str
    interests: str
