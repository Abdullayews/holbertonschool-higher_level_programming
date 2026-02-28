#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related classes.

    Subclasses must implement the area() method.
    """

    def area(self):
        """Raise an Exception since area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
