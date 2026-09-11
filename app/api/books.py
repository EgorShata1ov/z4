from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("/", response_model=List[schemas.BookRead], summary="Список книг")
def list_books(
    category_id: Optional[int] = Query(None, description="Фильтр по id категории"),
    db: Session = Depends(get_db),
):
    """Вернуть список книг. Можно отфильтровать по category_id."""
    return crud.get_books(db, category_id=category_id)


@router.get("/{book_id}", response_model=schemas.BookRead, summary="Книга по id")
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Вернуть одну книгу по id. 404 — если не найдена."""
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.post(
    "/",
    response_model=schemas.BookRead,
    status_code=status.HTTP_201_CREATED,
    summary="Создать книгу",
)
def create_book(payload: schemas.BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу. 400 — если указанной категории не существует."""
    if not crud.get_category(db, payload.category_id):
        raise HTTPException(status_code=400, detail="Указанной категории не существует")
    return crud.create_book(
        db,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        category_id=payload.category_id,
        url=payload.url or '',
    )


@router.put("/{book_id}", response_model=schemas.BookRead, summary="Обновить книгу")
def update_book(book_id: int, payload: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Обновить данные книги по id. 400 — если категория не существует, 404 — если книга не найдена."""
    if not crud.get_category(db, payload.category_id):
        raise HTTPException(status_code=400, detail="Указанной категории не существует")
    book = crud.update_book(
        db,
        book_id=book_id,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        category_id=payload.category_id,
        url=payload.url or '',
    )
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить книгу",
)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу по id. 404 — если не найдена."""
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return None