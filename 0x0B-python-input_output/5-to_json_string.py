#!/usr/bin/python3
"""
json to string module
"""
import json


def to_json_string(my_obj):
    """return Json object as string
    args:
        my_obj: object to convert
    return:
        object
    """

    return json.dumps(my_obj)
