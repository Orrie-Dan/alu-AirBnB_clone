#!/usr/bin/python3
"""
This module defines the BaseModel class that serves as the foundation
for all other classes in the project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines common attributes and methods
    for all other classes.
    """

    def __init__(self):
        """
        Initialize a new BaseModel instance.
        
        Sets up:
        - id: unique string identifier
        - created_at: datetime when instance was created
        - updated_at: datetime when instance was last updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of the BaseModel instance.
        
        Returns:
            str: String in format [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        This method should be called whenever the object is modified.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        
        Returns:
            dict: Dictionary containing all instance attributes with:
                  - All keys/values from self.__dict__
                  - __class__ key with the class name
                  - created_at and updated_at converted to ISO format strings
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        
        return obj_dict
