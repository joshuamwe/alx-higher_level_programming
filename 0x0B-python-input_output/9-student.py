#!/usr/bin/python3
"""defines class student"""


class Student:
    """initializes class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary rep of student instance"""
        return self.__dict__
