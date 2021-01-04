"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


def isUnique(string):
    """Return true/false if a string has all unique characters.

    >>> isUnique('abcdef')
    True
    >>> isUnique('hello')
    False
    >>> isUnique('Aabc')
    False
    """

    seen = set()

    for ch in string:
        if ch.lower() in seen:
            return False
        seen.add(ch.lower())

    return True


def isUniqueNoDS(string):
    """Return true/false if a string has all unique characters without the use of
    a data structure.

    >>> isUniqueNoDS('abcdef')
    True
    >>> isUniqueNoDS('hello')
    False
    >>> isUniqueNoDS('Aabc')
    False
    """

    sorted_str = sorted(string.lower())

    for i in range(1, len(sorted_str)):
        if sorted_str[i] == sorted_str[i-1]:
            return False

    return True
