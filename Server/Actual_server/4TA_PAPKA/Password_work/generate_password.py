"""Generate secure password"""
from string import ascii_letters, digits, punctuation
from random import choice


def generate_password(count, word=''):
    """Function to generate secure password
    :param count: Count of the password's symbols
    :param word: Starting word for the password(optional)
    :rtype: str or bool
    :return: Generated password or False if count > len(word)
    """
    # Get all symbols
    symbols = ascii_letters + digits + punctuation
    if len(word) > count:
        return False
    password = word

    # Generate password
    for i in range(len(password), count):
        password += choice(symbols)
    return password
