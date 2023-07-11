#!/usr/bin/python3
"""Defines a functions that writes into files"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of file to write in.
        text (str): The text to write into file.
    Returns:
        Returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
