from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from library.base.database import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    author = Column('author', String(32))
    article = Column('article', Integer)
    orders = relationship("Order", back_populates="orders")
