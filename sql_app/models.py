from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    orders = relationship("Order", back_populates="user")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    name = Column('name', String(32))
    author = Column('author', String(32))
    article = Column('article', Integer)

    orders = relationship("Order", back_populates="books")


class Librarian(Base):
    __tablename__ = 'librarians'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column('firstname', String(32))
    lastname = Column('lastname', String(32))
    passport_number = Column('passport_number', String(32))
    phone_number = Column('phone_number', String(32))

    orders = relationship("Order", back_populates="librarians")


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    librarian_id = Column(Integer, ForeignKey("librarians.id"), index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    email_address = Column(String, nullable=False, index=True)
    order_date = Column('order_date', Integer)
    return_date = Column('return_date', Integer)

    user = relationship("User", back_populates="orders")
    books = relationship("Book", back_populates="orders")
    librarians = relationship("Librarian", back_populates="orders")

# пробувати включити моделі які закоментовано, після зміни в коді видаляти базу і перезапускати
# всі айдішники зробити індексовані
