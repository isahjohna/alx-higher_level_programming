#!/usr/bin/python3

"""a function that prints all integers of a list,
in reversed order."""


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for e in range(len(my_list)):
            print("{:d}".format(my_list[e]))


""" Method 2
    if isinstance(my_list, list):
        for integer in reversed(my_list):
            print("{:d}".format(integer))"""
