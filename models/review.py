#!/usr/bin/python3
"""A Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class that inherits from the BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
