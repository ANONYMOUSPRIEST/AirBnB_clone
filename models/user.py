

#!/usr/bin/python3
"""A User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """A User class that inherits from the BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
