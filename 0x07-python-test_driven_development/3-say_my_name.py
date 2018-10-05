#!/usr/bin/python3
"""
Print string
"""
def say_my_name(first_name, last_name=""):
   """Concatenate both parameters and print
   Parameters:
   first_name = first name
   last_name = last name

   Local Variables:
   fullname = empty string

   Return: None
   """
    fullname = ""
    if first_name and type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif first_name and type(first_name) == str:
        fullname += first_name + " "
    if last_name and type(last_name) != str:
        raise TypeError('last_name must be a string')
    elif last_name and type(last_name) == str:
        fullname += last_name
    print("My name is {:s}".format(fullname))
