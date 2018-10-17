#!/usr/bin/python3
"""
read method
"""


def read_lines(filename="", nb_lines=0):
    """read n lines of text file
    args:
        filename: file to read
        nb_lines: n line
    return:
        na
    """
    line_num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line_num < nb_lines or not nb_lines or nb_lines < 0:
                print(line, end="")
            line_num += 1
