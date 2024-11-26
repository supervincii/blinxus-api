from pydantic import BaseModel
import uuid
from datetime import date

class User(BaseModel):
    id: uuid.UUID
    name: str
    birthday: date
    nationality: str
    interests: list[str] | None
    is_founder: bool
    is_influencer: bool
    is_service: bool

class Favorites(BaseModel):
    food: str
    interests: str
