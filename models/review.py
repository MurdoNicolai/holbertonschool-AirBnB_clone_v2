#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('place_id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user_id'), nullable=False)
    text = Column(String(1024), nullable=False)

    place = relationship("Place", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

Place.cities = relationship(
    "Review", order_by=Review.id, back_populates="place")
User.cities = relationship(
    "Review", order_by=Review.id, back_populates="user")
