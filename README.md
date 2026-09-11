# API каталога книг (FastAPI + SQLAlchemy + PostgreSQL)

Учебный проект: REST API для работы с книгами и категориями.

## Стек
- Python 3
- FastAPI + Uvicorn
- SQLAlchemy
- PostgreSQL
- Pydantic

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API будет доступно на http://127.0.0.1:8000

## Эндпоинты

### Служебные
- `GET /health` — проверка работоспособности

### Категории
- `GET /categories/` — список категорий
- `GET /categories/{id}` — категория по id
- `POST /categories/` — создать категорию
- `PUT /categories/{id}` — обновить категорию
- `DELETE /categories/{id}` — удалить категорию

### Книги
- `GET /books/` — список книг (фильтр `?category_id=`)
- `GET /books/{id}` — книга по id
- `POST /books/` — создать книгу
- `PUT /books/{id}` — обновить книгу
- `DELETE /books/{id}` — удалить книгу

## Документация
Swagger: http://127.0.0.1:8000/docs

## Скриншоты работы

- `examples/docs.png` — Swagger со всеми эндпоинтами
- `examples/request.png` — успешный запрос `GET /books/` (код 200)
- `examples/psql.png` — данные из таблиц `categories` и `books` в PostgreSQL