from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

engine = create_async_engine('sqlite+aiosqlite:///tasks.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

"""SQL"""


class Base(DeclarativeBase):
    pass


class TaskModel(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    tag: Mapped[str]
    description: Mapped[str]

"""Pydantic"""


class TaskSchema(BaseModel):
    tag: str
    title: str
    description: str

@app.post('/setup')
async def setup_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


@app.post('/tasks')
async def add_task(data: TaskSchema, session: SessionDep):
    new_task = TaskModel(tag=data.tag, title=data.title, description=data.description)
    session.add(new_task)
    await session.commit()
    return {"message": True}


#  TODO : add get request
@app.get('/tasks')
async def get_all_tasks():
    ...
