#!/usr/bin/python3
"""Defines class Rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle

        Args:
            width ([int]): [width of rectangle]
            height ([int]): [heigth of rectangle]
            x (int): [x coordinates of new rectangle]. Defaults to 0.
            y (int): [y coordinates of new rectangle]. Defaults to 0.
            id ([int]): [identity of new rectangle]. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the new value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the new value for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display the rectangle with character #"""
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print('#', end="")
                for j in range(self.width)]
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def to_dictionary(self):
        """returns a dictionary representation of the Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """Updates the Rectangle and assigns argument to attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y,)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
