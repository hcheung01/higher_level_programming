#!/usr/bin/python3
"""
write method
"""


def write_file(filename="", text=""):
    """write to file
    args:
        filename: file to manipulate
    text:
        text: string to write with
    return:
        number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
