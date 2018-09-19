#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
        else:
            continue
    return (max)
