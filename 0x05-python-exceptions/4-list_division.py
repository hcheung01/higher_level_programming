#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    index = 0
    while index < list_length:
        try:
            result = my_list_1[index] / my_list_2[index]
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        finally:
            new_list += [result]
        index += 1
    return new_list
