#!/usr/bin/python
"""Defines and object atribute lookup function."""


def lookup(obj):
    """Returns a list of the attributes and method of obj"""
    return dir(obj)