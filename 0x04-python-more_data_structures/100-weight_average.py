#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numero = 0
    denomi = 0

    for tup in my_list:
        numero += tup[0] * tup[1]
        denomi += tup[1]

    return (numero / denomi)

