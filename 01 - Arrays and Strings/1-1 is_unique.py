"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


def is_unique(string):
    """Return true/false if a string has all unique characters.

    >>> is_unique('abcdef')
    True
    >>> is_unique('hello')
    False
    >>> is_unique('Aabc')
    False
    """

    seen = set()

    for ch in string:
        if ch.lower() in seen:
            return False
        seen.add(ch.lower())

    return True


def is_unique_no_ds(string):
    """Return true/false if a string has all unique characters without the use of
    a data structure.

    >>> is_unique_no_ds('abcdef')
    True
    >>> is_unique_no_ds('hello')
    False
    >>> is_unique_no_ds('Aabc')
    False
    """

    sorted_str = sorted(string.lower())

    for i in range(1, len(sorted_str)):
        if sorted_str[i] == sorted_str[i-1]:
            return False

    return True
