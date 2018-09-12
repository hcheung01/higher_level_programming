#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    count = 0
    for i in str:
        if count is not n:
            copy += i
        count = count + 1
    return copy
