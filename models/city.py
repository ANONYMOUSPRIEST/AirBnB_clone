#!/usr/bin/python3
"""A City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """A City class that inherits from the BaseModel"""
    state_id = ''
    name = ''
