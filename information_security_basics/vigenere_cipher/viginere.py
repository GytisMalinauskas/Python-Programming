"""A module for implementing Viginere's cipher encryption and decryption"""

from ctypes import ArgumentError
from alphabet import Alphabet
from analysis import find_key_lenght, find_key
from caesar import caesar

def viginere(text: str,  alphabet: Alphabet, key: str = None, encrypt: bool = True):
    try:
        if encrypt and key:
            encrypted_chars = []
            key_index = 0
            for char in text:
                if char in alphabet: 
                    keychar_index = alphabet[key[key_index]]
                    encrypted_char = caesar(char, alphabet, keychar_index, encrypt=False)
                    encrypted_chars.append(encrypted_char)
                    key_index = (key_index + 1) % len(key)
                
                    encrypted_chars.append(char)
                    
            return "".join(encrypted_chars)
        
        elif not encrypt and not key:
            return find_key(find_key_lenght(text))
            
        else:
            raise ArgumentError("The arguments must be passed corectly.")
    except ArgumentError:
        exit()