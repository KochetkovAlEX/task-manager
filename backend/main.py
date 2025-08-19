from typing         import Annotated
from fastapi        import FastAPI, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy     import select
from database.model import *
from schema.model   import *


app = FastAPI()

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@app.post('/setup', tags=["SETUP"])
async def setup_database() -> None:
    """
    Async func for setup DB
    """
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


@app.post('/tasks', tags=["POST"])
async def add_task(data: TaskSchema, session: SessionDep):
    """
    Async func for adding tasks
    """
    try:
        new_task = TaskModel(tag=data.tag, title=data.title, description=data.description)
        session.add(new_task)
        await session.commit()
        return {
            "message": True
        }
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Task with this title already exists"
        )


@app.get('/tasks', tags=["GET"])
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


@app.put('/tasks/{task_title}', tags=["PUT"])
async def change_task_and_save(task_title: str, data: TaskSchema, session: SessionDep):
    """
    Async func for update task in DB
    """
    task_to_change = await session.scalar(select(TaskModel).where(TaskModel.title == task_title))

    if not task_to_change:
        return {"status": 404, "message": "Can`t found task"}

    task_to_change.title = data.title
    task_to_change.description = data.description
    task_to_change.tag = data.tag
    await session.commit()
    await session.refresh(task_to_change)
    return {"status": 200}


@app.delete("/tasks/{task_title}", tags=["DELETE"])
async def delete_task_by_title(task_title: str, session: SessionDep):
    """
    Async func for delete task by title
    """
    await session.delete(
        select(TaskModel).where(TaskModel.title == task_title)
    )
    await session.commit()
    return {"status": 200}


@app.get("/tasks/completed", tags=["GET"])
async def get_completed_tasks(session: SessionDep):
    """
    Async func for getting completed tasks
    """
    result = await session.execute(select(TaskModel).where(TaskModel.is_complete is True))
    completed_task = result.scalars().all()
    return {
        "status": 200,
        "data": completed_task
    }


@app.get("/tasks/{tag}", tags=["GET"])
async def get_tasks_with_tag(tag: str, session: SessionDep):
    """
    Async func for getting task by tag
    """
    result = await session.execute(select(TaskModel).where(TaskModel.tag == tag))
    tasks = result.scalars().all()
    return {
        "status": 200,
        "data": tasks
    }


@app.put('/tasks/{task_title}', tags=["PUT"])
async def make_task_completed(task_title: str, session: SessionDep):
    """
    Async func for making task completed
    """
    task_to_change = await session.scalar(select(TaskModel).where(TaskModel.title == task_title))
    task_to_change.is_complete = True
    await session.commit()
    await session.refresh(task_to_change)
    return {"status": 200}

