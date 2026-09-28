"""A module for implementing Viginere's cipher encryption and decryption"""

from ctypes import ArgumentError
from alphabet import Alphabet
from analysis import find_key_lenght, find_key

def viginere(text: str,  alphabet: Alphabet, key: str = None, encrypt: bool = True):
    try:
        if encrypt and key:
            ...
        elif not encrypt and not key:
            ...
        else:
            raise ArgumentError("The arguments must be passed corectly.")
    except ArgumentError:
        exit()