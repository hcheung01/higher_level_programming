#!/usr/bin/python3
"""
Method to check class
"""


def is_same_class(obj, a_class):
    """check for class if same type of object
    args:
        obj: object import
        a_class: class type
    Return:
        True or False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
