from app.db.db import engine, SessionLocal, Base
from app.db.models import Category, Book
from app.db.crud import create_category, create_book, get_category_by_title

def init_database():
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы")
    
    db = SessionLocal()
    
    try:
        categories = ["Программирование", "Художественная литература"]
        
        for cat_title in categories:
            existing = get_category_by_title(db, cat_title)
            if not existing:
                category = create_category(db, cat_title)
                print(f"Категория '{cat_title}' создана с ID: {category.id}")
            else:
                print(f"Категория '{cat_title}' уже существует")
        
        prog_cat = get_category_by_title(db, "Программирование")
        if prog_cat:
            books = [
                {"title": "Python. Полное руководство", "description": "Книга по Python для начинающих и профессионалов", "price": 1500.50, "category_id": prog_cat.id},
                {"title": "SQL для начинающих", "description": "Самоучитель по SQL с примерами", "price": 800.00, "category_id": prog_cat.id},
                {"title": "Алгоритмы и структуры данных", "description": "Фундаментальные алгоритмы для разработчиков", "price": 1200.00, "category_id": prog_cat.id}
            ]
            for book_data in books:
                book = create_book(db, **book_data, url='')
                print(f"Книга '{book.title}' добавлена")
        
        art_cat = get_category_by_title(db, "Художественная литература")
        if art_cat:
            books = [
                {"title": "Война и мир", "description": "Роман-эпопея Льва Толстого", "price": 900.00, "category_id": art_cat.id},
                {"title": "Преступление и наказание", "description": "Роман Федора Достоевского", "price": 750.50, "category_id": art_cat.id},
                {"title": "Мастер и Маргарита", "description": "Роман Михаила Булгакова", "price": 820.00, "category_id": art_cat.id}
            ]
            for book_data in books:
                book = create_book(db, **book_data, url='')
                print(f"Книга '{book.title}' добавлена")
        
        print("\nБаза данных успешно инициализирована!")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()