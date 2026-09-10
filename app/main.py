from app.db.db import SessionLocal
from app.db.models import Category, Book
from app.db.crud import get_all_categories, get_all_books

def display_data():
    db = SessionLocal()
    
    try:
        print("\n" + "="*60)
        print("КАТАЛОГ КНИГ")
        print("="*60)
        
        categories = get_all_categories(db)
        
        for category in categories:
            print(f"\nКатегория: {category.title}")
            print("-"*50)
            
            books = category.books
            if books:
                for book in books:
                    print(f"  Название: {book.title}")
                    print(f"     Описание: {book.description}")
                    print(f"     Цена: {book.price:.2f} руб.")
                    print()
            else:
                print("  В этой категории нет книг")
        
        all_books = get_all_books(db)
        print("="*60)
        print(f"Всего книг: {len(all_books)}")
        print(f"Всего категорий: {len(categories)}")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    display_data()