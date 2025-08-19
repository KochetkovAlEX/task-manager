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
async def add_task(data: TaskSchema, session: SessionDep):
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
async def get_all_tasks(session: SessionDep):
    """
    Async func for reading all tasks from DB
    """
    result = await session.execute(select(TaskModel))
    tasks = result.scalars().all()
    return {
        "status": 200,
        "data": tasks
    }


@app.put('/tasks/{task_title}')
async def change_task_and_save(task_title: str, data: TaskSchema, session: SessionDep):
    """
    Async func for update task in DB
    """
    task_to_change = await session.scalar(select(TaskModel).where(TaskModel.title == task_title))

    if not task_to_change:
        return {"message": False, "description": "Can`t find task"}

    task_to_change.title = data.title
    task_to_change.description = data.description
    task_to_change.tag = data.tag
    await session.commit()
    await session.refresh(task_to_change)
    return {"message": True}


@app.delete("/tasks/{task_title}")
async def delete_task_by_title(task_title: str, session: SessionDep):
    """
    Async func for delete task by title
    """
    await session.delete(
        select(TaskModel).where(TaskModel.title == task_title)
    )
    await session.commit()
    return {"message":True}
