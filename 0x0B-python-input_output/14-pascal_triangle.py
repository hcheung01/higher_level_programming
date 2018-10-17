#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """calculate pascal
    args:
        n: value
    return
        list
    """
    i = 0
    outerlist = []
    for num in range(n):
        if i < n:
            outerlist.append([11**i])
        i += 1
    return outerlist
