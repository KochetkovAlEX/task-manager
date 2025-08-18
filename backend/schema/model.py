from pydantic import BaseModel
from datetime import datetime
# Pydantic schema
class TaskSchema(BaseModel):
    tag: str
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    tag: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True  # Ранее называлось orm_mode=True