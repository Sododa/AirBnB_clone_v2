#!/usr/bin/python3
""" Place base Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)
"""
Represents the many to many relationship table
"""


class Place(BaseModel, Base):
    """ place to stay """
    __tablename__ = 'places'
    city_id = Column(
            String(60), ForeignKey('cities.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(
        String(1024), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(
        Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(
        Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []
    reviews = relationship(
        'Review',
        cascade="all, delete, delete-orphan",
        backref='place'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities'
        )
    else:
        @property
        def amenities(self):
            """defines amenities the amenities of"""
