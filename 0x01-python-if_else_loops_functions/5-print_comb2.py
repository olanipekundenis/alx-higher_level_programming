#!/usr/bin/python3

"""prints numbers in range 0-100"""
for fig in range(0, 100):
    if fig == 99:
        print("{}".format(fig))
    else:
        print("{:02}".format(fig), end=", ")
