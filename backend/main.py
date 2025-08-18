from typing         import Annotated
from fastapi        import FastAPI, Depends
from database.model import *
from schema.model   import *

app = FastAPI()

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@app.post('/setup')
async def setup_database() -> None:
    """
    Async func for setup DB
    """
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


@app.post('/tasks')
async def add_task(data: TaskSchema, session: SessionDep) -> dict:
    """
    Async func for adding tasks
    """
    new_task = TaskModel(tag=data.tag, title=data.title, description=data.description)
    session.add(new_task)
    await session.commit()
    return {
        "message": True
    }


@app.get('/tasks')
async def get_all_tasks(session: SessionDep, response_model=TaskResponse):
    """
    Async func for reading all tasks from DB
    """
    result = await session.execute(select(TaskModel))
    tasks = result.scalars().all()
    return {
        "status": 200,
        "data": tasks
    }
