#!/usr/bin/python3
"""Module that converts a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Return a Python object from a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
