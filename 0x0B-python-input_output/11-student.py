#!/usr/bin/python3
"""
Definition of the class Student
"""


class Student:
    """
    A class that represents a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instatiation with first_name, last_name and age

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """

        self.firs_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the class instance.
        If attrs is supplied, represents only those attributes

        Args:
            attrs (list): (Optional) The attributes to represent
        """

        if type(attrs) is list and
            all(type(ele) is str for ele in attr):
                return {k: getattr(self, k) for k in attr if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the class instance

        Args:
            json (dict): The key/value pairs to replace attributes with
        """
        for k, v in json.items():
            setattr(self, k, v)


