"""A module for implementing Viginere's cipher encryption and decryption"""

from ctypes import ArgumentError
from alphabet import Alphabet
from analysis import find_key_lenght, find_key
from caesar import caesar
from itertools import cycle

def viginere(text: str,  alphabet: Alphabet, key: str = None, encrypt: bool = True):
    try:
        if encrypt and key:
            encrypted_chars = []
            for char, keychar in zip(text, cycle(key)):
                keychar_index = alphabet[keychar]
                encrypted_char = caesar(char, alphabet, keychar_index)
                encrypted_chars.append(encrypted_char)
            return "".join(encrypted_chars)
        
        elif not encrypt and not key:
            find_key(find_key_lenght(text))
            
        else:
            raise ArgumentError("The arguments must be passed corectly.")
    except ArgumentError:
        exit()