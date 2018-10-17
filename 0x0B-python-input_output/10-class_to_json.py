#!/usr/bin/python3
"""
Json module
"""


def class_to_json(obj):
    """returns dict description data structure
    args:
        obj: object
    return:
        object serialized
    """
    return vars(obj)
