#!/usr/bin/python3
"""Module that defines Square with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square with Square string representation."""

    def __init__(self, size):
        """Initialize Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
