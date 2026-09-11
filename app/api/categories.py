from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/categories", tags=["Категории"])


@router.get("/", response_model=List[schemas.CategoryRead], summary="Список категорий")
def list_categories(db: Session = Depends(get_db)):
    """Вернуть список всех категорий."""
    return crud.get_all_categories(db)


@router.get("/{category_id}", response_model=schemas.CategoryRead, summary="Категория по id")
def get_category(category_id: int, db: Session = Depends(get_db)):
    """Вернуть одну категорию по её id. 404 — если не найдена."""
    cat = crud.get_category(db, category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return cat


@router.post(
    "/",
    response_model=schemas.CategoryRead,
    status_code=status.HTTP_201_CREATED,
    summary="Создать категорию",
)
def create_category(payload: schemas.CategoryCreate, db: Session = Depends(get_db)):
    """Создать новую категорию. 400 — если категория с таким названием уже есть."""
    if crud.get_category_by_title(db, payload.title):
        raise HTTPException(status_code=400, detail="Категория с таким названием уже существует")
    return crud.create_category(db, payload.title)


@router.put("/{category_id}", response_model=schemas.CategoryRead, summary="Обновить категорию")
def update_category(category_id: int, payload: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    """Обновить название категории по id. 404 — если не найдена."""
    cat = crud.update_category(db, category_id, payload.title)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return cat


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить категорию",
)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Удалить категорию по id. 404 — если не найдена."""
    cat = crud.delete_category(db, category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return None