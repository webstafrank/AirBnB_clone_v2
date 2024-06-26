#!usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship to Place
    places = relationship("Place", back_populates="city", cascade="all, delete, delete-orphan")
