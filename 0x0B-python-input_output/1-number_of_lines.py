#!/usr/bin/python3
"""
Line function
"""


def number_of_lines(filename=""):
    """number of lines from file
    args:
        filename: file to read
    return:
        number of lines
    """
    line_num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line_num += 1
    return line_num
