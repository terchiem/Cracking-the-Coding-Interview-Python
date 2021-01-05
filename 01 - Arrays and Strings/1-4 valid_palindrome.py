"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words.
"""


def valid_palindrome(string):
    """Returns true/false if the input string can be rearranged into a valid
    palindrome.

    >>> valid_palindrome('Tact Coa')
    True

    >>> valid_palindrome('abcdef')
    False

    >>> valid_palindrome('abcab')
    True

    >>> valid_palindrome('aaaaa')
    True

    >>> valid_palindrome('')
    True
    """

    count = {}
    simplified_string = string.replace(' ', '').lower()

    for ch in simplified_string:
        count[ch] = count.get(ch, 0) + 1

    odd_found = False
    for ch in count.keys():
        if count[ch] % 2 != 0:
            if odd_found:
                return False
            odd_found = True

    return True
