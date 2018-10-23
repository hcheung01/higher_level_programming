#!/usr/bin/python3
import json
"""
Class Module
"""


class Base:
    """ base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initiation method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_validator2(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string"""
        if list_dictionaries is None:
            return ([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """json to string static method"""
        if json_string is None:
            return ([])
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to a file"""
        jsonstr = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        if jsonstr is None:
            jsonstr = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(jsonstr)

    @classmethod
    def create(cls, **dictionary):
        """return instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        with open(cls.__name__ + '.json') as f:
            dictss = cls.from_json_string(f.read())
            if dictss:
                listme = [cls.create(**x) for x in dictss]
                return listme
            else:
                return []
