"""
URLify: Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
"""


def urlify(string, length):
    """Return an input string with all spaces replaced with '%20'

    >>> urlify('Mr John Smith    ', 13)
    'Mr%20John%20Smith'

    >>> urlify('abcdefg', 7)
    'abcdefg'

    >>> urlify('a b c d e f          ', 11)
    'a%20b%20c%20d%20e%20f'

    """
    char_array = list(string)

    ch_index = length - 1
    str_index = len(string) - 1

    while ch_index >= 0:
        if char_array[ch_index] == ' ':
            char_array[str_index] = '0'
            char_array[str_index-1] = '2'
            char_array[str_index-2] = '%'
            str_index -= 3
        else:
            char_array[str_index] = char_array[ch_index]
            str_index -= 1
        ch_index -= 1

    return ''.join(char_array)
