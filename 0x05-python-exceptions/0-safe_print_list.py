#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts from a given list
    Args:
        my_list (list): The list that the elements are printed from
        x (int): The number of elements of my_list[i] to be printed
    Returns:
        Returns printed number of elements
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
