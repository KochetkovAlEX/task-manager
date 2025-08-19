from pydantic import BaseModel
from datetime import datetime
# Pydantic schema
class TaskSchema(BaseModel):
    tag: str
    title: str
    description: str
    created_at: datetime
