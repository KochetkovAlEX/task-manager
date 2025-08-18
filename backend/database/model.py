from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm         import DeclarativeBase, Mapped, mapped_column
from datetime               import datetime
from sqlalchemy             import select, func

engine = create_async_engine('sqlite+aiosqlite:///tasks.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class TaskModel(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    tag: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

# TODO: Реализуй механизм перевода активной задачи в список выполненных и добавь отображение выполненных.
# Скорее всего тебе понадобится сделать на js функцию перерисовки страницы после нажатия кнопки ADD или кнопки "Done"(рабочее название)
"""
class CompletedTaskModel(Base):
    __tablename__ = "completed_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    tag: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    completed_at: Mapped[datetime] = mapped_column(nullable=False)
"""
# async func for getting session
async def get_session():
    async with new_session() as session:
        yield session

