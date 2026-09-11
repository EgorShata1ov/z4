from sqlalchemy.orm import Session
from app.db.models import Category, Book


# ---------- Категории ----------

def create_category(db: Session, title: str):
    """Создать новую категорию."""
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_title(db: Session, title: str):
    """Найти категорию по названию (для проверки уникальности)."""
    return db.query(Category).filter(Category.title == title).first()


def get_all_categories(db: Session):
    """Получить список всех категорий."""
    return db.query(Category).all()


def get_category(db: Session, category_id: int):
    """Получить категорию по id."""
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db: Session, category_id: int, title: str):
    """Обновить название категории. None — если категория не найдена."""
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    db_category.title = title
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    """Удалить категорию. None — если не найдена."""
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category


# ---------- Книги ----------

def create_book(db: Session, title: str, description: str, price: float,
                category_id: int, url: str = ''):
    """Создать новую книгу."""
    db_book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_all_books(db: Session):
    """Получить все книги."""
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    """Получить книгу по id."""
    return db.query(Book).filter(Book.id == book_id).first()


def get_books(db: Session, category_id: int | None = None):
    """Получить книги; если указан category_id — только из этой категории."""
    query = db.query(Book)
    if category_id is not None:
        query = query.filter(Book.category_id == category_id)
    return query.all()


def update_book(db: Session, book_id: int, title: str, description: str,
                price: float, category_id: int, url: str = ''):
    """Обновить данные книги. None — если книга не найдена."""
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db_book.title = title
    db_book.description = description
    db_book.price = price
    db_book.category_id = category_id
    db_book.url = url
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    """Удалить книгу. None — если не найдена."""
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book