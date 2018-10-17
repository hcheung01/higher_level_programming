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
    lists = []
    if n <= 0:
        return lists
    while i < n:
        lists.append([11**i])
        i += 1
    return lists
