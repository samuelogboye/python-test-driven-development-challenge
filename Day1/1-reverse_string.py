#!/usr/bin/python3
"""Defines a String Reversing function."""


def reverse_string(string):
    """Reverse a string

    Args:
         string
    Raises:
         TypeError: if string is not a string
         ValueError: if string is empty
    Returns:
         The reversed string
    """

    if string == "":
        raise ValueError("string can't be empty")

    if not isinstance(string, str):
        raise TypeError("string must be a Str")

    reversed_string = ''.join(string[i] for i in range(len(string)-1, -1, -1))
    return reversed_string
