#!/usr/bin/python3
"""
City module
Defines the City class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city within a state.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
        self.state_id = ""
