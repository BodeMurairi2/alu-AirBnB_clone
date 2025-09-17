#!/usr/bin/python3
"""
Place module
Defines the Place class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class representing accommodation listings.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Place instance.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
