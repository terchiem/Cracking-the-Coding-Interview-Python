"""
Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other.
"""


def check_permutation(string1, string2):
    """Returns true/false if the argument strings are permuations
    of each other.

    >>> check_permutation('abc', 'cba')
    True

    >>> check_permutation('abc', 'def')
    False
    """
    hash1 = {}
    hash2 = {}

    for ch in string1:
        hash1[ch] = hash1.get(ch, 0) + 1

    for ch in string2:
        hash2[ch] = hash2.get(ch, 0) + 1

    for ch in hash1.keys():
        if hash1.get(ch) != hash2.get(ch):
            return False

    return True
