#!/usr/bin/python3
"""Module that defines a LockedClass."""


class LockedClass:
    """A class that only allows first_name as instance attribute."""
    __slots__ = ['first_name']
