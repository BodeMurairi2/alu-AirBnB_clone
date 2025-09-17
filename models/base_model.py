#!/usr/bin/python3
"""
BaseModel module
Defines the BaseModel class that other models will inherit from.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models.
    Provides id, created_at, updated_at attributes
    and basic methods for serialization and updating.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def save(self):
        """
        Update updated_at timestamp when the object is changed.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }
