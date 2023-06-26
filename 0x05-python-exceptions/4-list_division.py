#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides my_list_1 by my_list_2
    Args:
        my_list_1 (list): Represents the first list.
        my_list_2 (list): Represents the second list.
        list_length (int): Represents the number of elements to divide.
    Returns:
        Returns the length of list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
