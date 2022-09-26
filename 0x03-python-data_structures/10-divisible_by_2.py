#!/usr/bin/python3

"""a function that finds all multiples of 3 in a list."""


def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if (i % 2):
            new_list.append(False)
        else:
            new_list.append(True)
    return new_list
