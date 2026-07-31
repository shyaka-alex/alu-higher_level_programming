#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

This module provides matrix division functionality with validation
of matrix structure and division parameters.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (int or float, not zero).

    Returns:
        list: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is invalid or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
