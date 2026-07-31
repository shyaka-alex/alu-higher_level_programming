#!/usr/bin/python3
"""Module that provides a lookup function for object attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of available attributes and methods.
    """
    return dir(obj)
