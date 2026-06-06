from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="user")

    orders = relationship("Order", back_populates="owner")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.now())

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="orders")
