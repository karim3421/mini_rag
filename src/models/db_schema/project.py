from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1)

    @field_validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError("prject_id must be alphanumeric")
        
        return value
    

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indecies(cls):
        return [
            {
                "key": [("project_id", 1)],
                "name": "project_id_index_1", 
                "unique": True
            }
        ]