#!/usr/bin/python3
"""Module that defines Square inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square using Rectangle."""

    def __init__(self, size):
        """Initialize Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
