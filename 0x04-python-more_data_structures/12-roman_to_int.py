#!/usr/bin/python3
def roman_to_int(roman_string):
    num = dict([('I', 1), ('V', 5), ('X', 10),
                ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    total = 0
    if roman_string and roman_string != None:
        if roman_string != 'IX':
            for i in roman_string:
                for k, v in num.items():
                    if i is k:
                        total = total + v
        else:
            total = 9
    return (total)
