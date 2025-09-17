#!/usr/bin/python3
"""
State module
Defines the State class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representing a state within a country.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
