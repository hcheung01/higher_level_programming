#!/usr/bin/python3
"""
create object module
"""
import json


def load_from_json_file(filename):
    """create object method
    args:
        filename: file to deserialize
    return:
        object
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
