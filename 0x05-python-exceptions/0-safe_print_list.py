#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i += 1
    except:
        pass
    print()
    return i
