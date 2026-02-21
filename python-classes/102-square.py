#!/usr/bin/python3
"""Module that defines a Square class with comparison operators."""


class Square:
    """Defines a square that supports area-based comparisons."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int or float): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __lt__(self, other):
        """Less than comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on area."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equality comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison based on area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on area."""
        return self.area() >= other.area()
