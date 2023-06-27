#!/usr/bin/python3
"""Represent a class Square."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the new Square.

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("if size is not an integer")
        elif size < 0:
            raise ValueError("if size is < 0")
        self.__size = size
