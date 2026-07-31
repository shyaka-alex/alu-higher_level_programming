#!/usr/bin/python3
"""Module that defines MyInt, a rebel integer class."""


class MyInt(int):
    """A class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Return True if values are not equal (inverted)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True if values are equal (inverted)."""
        return super().__eq__(other)
