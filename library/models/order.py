from sqlalchemy import Column, ForeignKey, Integer, String

from library.base.database import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    librarian_id = Column(Integer, ForeignKey("librarians.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    email_address = Column(String, nullable=False)
    order_date = Column('order_date', Integer)
    return_date = Column('return_date', Integer)
