from typing import Optional
from pydantic import BaseModel, Field
from db.database import PyObjectId,ObjectId

class CommentBase(BaseModel):
    author: str
    text: str

class CommentCreate(CommentBase):
    pass

class CommentInDB(CommentBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    artwork_id: PyObjectId

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True


class ArtworkBase(BaseModel):
    title: str
    description: Optional[str] = None
    artist_name: str

class ArtworkCreate(ArtworkBase):
    pass

class ArtworkInDB(ArtworkBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
