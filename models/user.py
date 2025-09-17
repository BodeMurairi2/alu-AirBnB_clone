#!/usr/bin/python3
"""
User module
Defines the User class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class representing a system user.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
