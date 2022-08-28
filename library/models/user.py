from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from library.base.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column('firstname', String(32))
    lastname = Column('lastname', String(32))
    ticket_number = Column('ticket_number', Integer)
    email_address = Column('email_address', String(32), nullable=False)
    orders = relationship("Order", back_populates="orders")
