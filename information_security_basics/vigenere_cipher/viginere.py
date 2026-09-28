"""A module for implementing Viginere's cipher encryption and decryption"""

from alphabet import Alphabet
from analysis import find_key_lenght, find_key
from caesar import caesar

def viginere(
    text: str,
    alphabet: Alphabet,
    decrypt: bool = False,
    is_find_key: bool = False,
    key: str = None):
    try:
        if decrypt and key:
            encrypted_chars = []
            key_index = 0
            for char in text:
                is_upper = char != char.lower()
                keychar_index = alphabet[key[key_index]]
                if is_upper:
                    encrypted_char = caesar(char.lower(), alphabet, keychar_index, encrypt=False).upper()
                else:
                    encrypted_char = caesar(char, alphabet, keychar_index, encrypt=False)
                encrypted_chars.append(encrypted_char)
                key_index = (key_index + 1) % len(key)
            else:
                encrypted_chars.append(char)
                    
            return "".join(encrypted_chars)
        
        elif is_find_key and not key:
            return find_key(find_key_lenght(text))
            
        else:
            raise ValueError("Provide a key when encrypting, or omit it when decrypting.")
    except ValueError:
        exit()