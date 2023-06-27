#!/usr/bin/python3
"""Represents a class Square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the new square.

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("if size is not an integer")
        elif size < 0:
            raise ValueError("if size is no >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
