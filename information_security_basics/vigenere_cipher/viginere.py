"""A module for implementing Viginere's cipher encryption and decryption"""

from alphabet import Alphabet
from analysis import find_key_lenght, find_key

def viginere(text: str, key: str, alphabet: Alphabet, encrypt: bool = True):
    find_key(find_key_lenght)