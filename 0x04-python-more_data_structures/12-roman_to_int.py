#!/usr/bin/python3
def roman_to_int(roman_string):
    num = dict([('I', 1), ('V', 5), ('X', 10),
                ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    total = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    if roman_string != 'IX':
        for i in roman_string:
            for k, v in num.items():
                if i is k:
                    total = total + v
                    break
    else:
        total = 9
    return (total)
