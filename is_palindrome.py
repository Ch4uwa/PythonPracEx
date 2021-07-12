
phrase = 'abba'


def is_palindrome(phrase):
    return True if phrase.find(phrase[::-1]) == 0 else False
