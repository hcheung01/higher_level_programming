#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [[num, replace][num is search] for num in my_list]
