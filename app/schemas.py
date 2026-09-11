from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List


# ---------- Категории ----------

class CategoryBase(BaseModel):
    """Базовая схема категории."""
    title: str = Field(..., description="Название категории", examples=["Фантастика"])


class CategoryCreate(CategoryBase):
    """Схема для создания категории."""
    pass


class CategoryUpdate(CategoryBase):
    """Схема для обновления категории."""
    pass


class CategoryRead(CategoryBase):
    """Схема ответа с данными категории."""
    id: int = Field(..., description="Уникальный идентификатор категории")
    # from_attributes=True — чтобы Pydantic умел читать поля объекта SQLAlchemy
    model_config = ConfigDict(from_attributes=True)


# ---------- Книги ----------

class BookBase(BaseModel):
    """Базовая схема книги."""
    title: str = Field(..., description="Название книги", examples=["Дюна"])
    description: Optional[str] = Field(None, description="Описание книги")
    price: float = Field(..., description="Цена книги", examples=[800.0])
    url: Optional[str] = Field('', description="Ссылка на книгу")
    category_id: int = Field(..., description="id категории, к которой относится книга")


class BookCreate(BookBase):
    """Схема для создания книги."""
    pass


class BookUpdate(BookBase):
    """Схема для обновления книги."""
    pass


class BookRead(BookBase):
    """Схема ответа с данными книги."""
    id: int = Field(..., description="Уникальный идентификатор книги")
    model_config = ConfigDict(from_attributes=True)