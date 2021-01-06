"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits) away.
"""


def one_away(str1, str2):
    """Returns true/false if the two input strings are one edit away
    from each other.

    >>> one_away('pale', 'ple')
    True

    >>> one_away('pale', 'pales')
    True

    >>> one_away('pale', 'bale')
    True

    >>> one_away('pale', 'bake')
    False

    >>> one_away('pale', 'pls')
    False

    >>> one_away('pale', 'pa')
    False

    >>> one_away('pale', 'pa')
    False
    """

    len_diff = abs(len(str1) - len(str2))

    if len_diff > 1:
        return False

    # Walk through each string to find errors
    i = 0
    j = 0
    error_found = False

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if error_found:
                return False

            error_found = True
            if len_diff == 1:
                if len(str1) > len(str2):
                    j -= 1
                else:
                    i -= 1

        i += 1
        j += 1

    return True
