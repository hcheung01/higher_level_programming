#!/usr/bin/python3
"""
Attribute lookup
"""


def lookup(obj):
    """Lookup all attributes in Class

    Args:
        obj: object class
    Returns:
        Na
    """
    return [i for i in dir(obj)]
