#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer given this format "{:d}".format().

    Args:
        value (int): Represents the integer to be printed

    Returns:
        Returns a TypeError or ValueError if - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
