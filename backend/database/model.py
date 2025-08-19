from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine('sqlite+aiosqlite:///tasks.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class TaskModel(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    tag: Mapped[str]
    description: Mapped[str]
    is_complete: Mapped[bool] = mapped_column(default=False)

    # created_at: Mapped[datetime] = mapped_column(server_default=func.now())


# TODO: Реализуй механизм перевода активной задачи в список выполненных и добавь отображение выполненных.
# Скорее всего тебе понадобится сделать на js функцию перерисовки страницы после нажатия кнопки ADD или кнопки "Done"(рабочее название)
async def get_session():
    """
    Async func for getting session
    """
    async with new_session() as session:
        yield session
