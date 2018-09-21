#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newC = a_dictionary.copy()
    for i, j in newC.items():
        newC[i] = j * 2
    return (newC)
