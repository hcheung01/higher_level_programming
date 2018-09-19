#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    test = []
    for i in my_list:
        if i % 2 is 0:
            test = test + [True]
        else:
            test = test + [False]
    return test
