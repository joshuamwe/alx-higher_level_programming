#!/usr/bin/python3
"""Defines class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of Square

        Args:
            size ([int]): [new size of the square]
            x (int, optional): [x coordinates of square]. Defaults to 0.
            y (int, optional): [y coordinates of square]. Defaults to 0.
            id ([int], optional): [identity of the square]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y,
                                                 self.height)

    def to_dictionary(self):
        """return a dictionary representation of square"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Update the square"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == 'size':
                    self.size = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val
