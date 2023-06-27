#!/usr/bin/python3
"""Represents a class Square."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """reutrns the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("error if size is not an int")
        elif value < 0:
            raise ValueError("error if size is not >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
