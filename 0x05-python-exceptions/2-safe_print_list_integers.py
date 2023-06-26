#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list which is set to 0
    Args:
        my_list (list): Represents the list of elements to print
        x (int): Represents the number of my_list to print.
    Returns:
        Represents the number of elements that is printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
