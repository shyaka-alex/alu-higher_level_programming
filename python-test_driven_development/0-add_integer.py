#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides a simple addition function that works with
integers and floats, casting floats to integers before adding.
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    a and b must be integers or floats. Floats are cast to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Returns:
        int: The integer addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
