#!/usr/bin/python3

if __name__ == "__main__":

    """Prints addition of args parsed"""

    import sys

    sum_tot = 0
    for i in range(len(sys.argv) - 1):
        sum_tot += int(sys.argv[i + 1])
    print("{}".format(sum_tot))
