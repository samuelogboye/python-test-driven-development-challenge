#!/usr/bin/python3


def count_vowels(string):
    """A function that returns the number of
    vowel in the string"""
    if not isinstance(string, str):
        raise TypeError("The input should be a string.")
    vowel = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    return count
