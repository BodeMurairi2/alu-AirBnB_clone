#!/usr/bin/python3
"""
Amenity module
Defines the Amenity class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing services or features offered.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity instance.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
