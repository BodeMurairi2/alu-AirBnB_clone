#!/usr/bin/python3
"""
Review module
Defines the Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing user reviews for a place.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Review instance.
        """
        super().__init__(*args, **kwargs)
        self.text = ""
        self.user_id = ""
        self.place_id = ""
