#!/usr/bin/python3
"""
Definition of the class Student
"""


class Student:
    """
    A simple Student class to represent a Student
    """

    def __int__(self, first_name, last_name, age):
        """
        Instatiation with first_name, last_name and age

        Args:
            first_name (str): student's first name
            last_name (str): student's last_name
            age (int): student's age
        """

        self.firs_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the class instance
        """
        return self.__dict__


