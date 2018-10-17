#!/usr/bin/python3
"""
append module
"""


def append_after(filename="", search_string="", new_string=""):
    """append method"""

    stringme = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            stringme += line
            if search_string in line:
                stringme += new_string
    with open(filename, mode="w") as f:
        f.write(stringme)
