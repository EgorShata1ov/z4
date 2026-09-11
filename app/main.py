from fastapi import FastAPI

from app.db.db import Base, engine
from app.api import books, categories

# На всякий случай создаём таблицы, если их ещё нет в БД
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API каталога книг",
    description="Учебный API для работы с книгами и категориями (FastAPI + SQLAlchemy + PostgreSQL)",
    version="1.0.0",
)

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["Служебные"], summary="Проверка работоспособности")
def health():
    """Простой эндпоинт для проверки, что сервис жив."""
    return {"status": "ok"}
