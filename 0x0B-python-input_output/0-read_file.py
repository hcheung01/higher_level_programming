#!/usr/bin/python3
"""
Read file function
"""


def read_file(filename=""):
    """read a file
    args:
        filename: file to manipulate
    return:
        na
    """

    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
