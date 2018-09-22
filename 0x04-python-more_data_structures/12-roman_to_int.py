#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    for i in range(len(roman_string)):
        value = nums[roman_string[i]]
        if i + 1 < len(roman_string) and nums[roman_string[i + 1]] > value:
            sum -= value
        else:
            sum += value
    return sum
