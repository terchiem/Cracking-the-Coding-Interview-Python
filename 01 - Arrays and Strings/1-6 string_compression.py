"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2blc5a3. If the "compressed" string would not become smaller
than the original string, your method should return the original string. You
can assume the string has only uppercase and lowercase letters (a - z).
"""


def string_compression(string):
    """Returns a "compressed" string where each characters are followed by
    the count of repetition. If the "compressed" string is not smaller than
    the input string, return the original string instead.

    >>> string_compression('abc')
    'abc'

    >>> string_compression('aaaabbbc')
    'a4b3c1'

    >>> string_compression('aaabbc')
    'aaabbc'

    >>> string_compression('aaaaaaaaaa')
    'a10'
    """

    compressed = ''
    current_ch = string[0]
    count = 1
    i = 1

    while i < len(string):
        if string[i] != current_ch:
            compressed += current_ch + str(count)
            current_ch = string[i]
            count = 1
        else:
            count += 1
        i += 1

    compressed += current_ch + str(count)

    return compressed if len(compressed) < len(string) else string
