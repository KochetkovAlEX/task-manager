from pydantic import BaseModel

# Pydantic schema
class TaskSchema(BaseModel):
    tag: str
    title: str
    description: str

