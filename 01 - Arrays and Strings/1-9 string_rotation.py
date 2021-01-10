"""
String Rotation:Assume you have a method isSubstring which checks if one word
is a substring of another. Given two strings, sl and s2, write code to check
if s2 is a rotation of sl using only one call to isSubstring
(e.g., "waterbottle" is a rotation of "erbottlewat").
"""


def is_substring(s1, s2):
    """Returns true/false if one string is a substring of the other.

    >>> is_substring('abcdefgh', 'def')
    True

    >>> is_substring('abcdefgh', 'cat')
    False

    >>> is_substring('aaabbbbccccc', 'abbbbc')
    True
    """
    string_to_check = s1[:(len(s1)-len(s2)+1)]

    for i, ch in enumerate(string_to_check):
        if ch == s2[0] and s1[i:i+len(s2)] == s2:
            return True

    return False


def string_rotation(s1, s2):
    """Returns true/false if one string is a rotation of the other.

    >>> string_rotation('waterbottle', 'erbottlewat')
    True

    >>> string_rotation('abc', 'cba')
    False

    >>> string_rotation('abc', 'bca')
    True

    >>> string_rotation('aaabac', 'abacaa')
    True

    >>> string_rotation('aaabbbb', 'baaaabb')
    False
    """

    return is_substring(s1+s1, s2)
