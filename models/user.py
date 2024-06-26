#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    # Relationship to Place
    places = relationship("Place", back_populates="user", cascade="all, delete, delete-orphan")

