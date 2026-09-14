from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)

    books = relationship('Book', back_populates='category', passive_deletes=True)

    def __repr__(self):
        return f"<Category(id={self.id}, title='{self.title}')>"


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False, default=0)
    url = Column(String, default='')
    category_id = Column(
        Integer,
        ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False,
    )

    category = relationship('Category', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', price={self.price})>"