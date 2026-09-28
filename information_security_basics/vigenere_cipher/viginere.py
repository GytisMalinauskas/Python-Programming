"""A module for implementing Viginere's cipher encryption and decryption"""

from alphabet import Alphabet
from analysis import find_key_lenght, find_key

def viginere(text: str,  alphabet: Alphabet, key: str = None, encrypt: bool = True):
    if encrypt and key:
        