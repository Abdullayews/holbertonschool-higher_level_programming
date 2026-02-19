#!/usr/bin/python3
"""
Module for add_integer function.

This module provides a function to add two integers.
It handles both integers and floats.
"""


def add_integer(a, b=98):
    """
    Add two integers.
    
    Cast floats to integers before adding.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if a != a or a == float('inf') or a == float('-inf'):
        raise ValueError("cannot convert float infinity to integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise ValueError("cannot convert float infinity to integer")
    
    return int(a) + int(b)
