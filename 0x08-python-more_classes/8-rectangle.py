#!/usr/bin/python3
"""
Definition of a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class

    Atributes:
        number_of_instances (int): The number of Rectangle instances
        print_symbol (str): A symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiation with width and height

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def area(self):
        """
        Calculates the area of the rectangle

        Return:
            Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Return:
            Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """
        Getter

        Return:
            Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value (int): value to be set as width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        Return:
            None
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter

        Return:
            Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value (int): value to be set as height

        Raises:
            TypeError: If value is not an integer
            ValueError:If value is less than 0

        Return:
            None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Returns a printed rectangle

        Return:
            A printed rectangle with `#`
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        sy = str(self.print_symbol)
        return ((sy * self.__width + '\n') * self.__height)[:-1]

     def __repr__(self):
        """
        Returns the string representation of the rectangle

        Return:
            A string representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message after deletion of a Rectangle instance

        Return:
            A string
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checks which rectangle is bigger than the other based on their area

        Args:
            rect_1 (Rectangle): A Rectangle
            rect_2 (Rectangle): A Rectangle

        Raises:
            TypeError: If either rect_1 or rect_2 is not type `Rectangle`

        Return:
            rect_1 if its area is greater than that of rect_2, otherwise rect_2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

