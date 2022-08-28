from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from library.base.database import Base


class Librarian(Base):
    __tablename__ = 'librarians'
    id = Column(Integer, primary_key=True)
    firstname = Column('firstname', String(32))
    lastname = Column('lastname', String(32))
    passport_number = Column('passport_number', String(32))
    phone_number = Column('phone_number', String(32))
    orders = relationship("Order", back_populates="orders")
