"""A module for implementing Viginere's cipher decryption and finding a key"""

from alphabet import Alphabet
from analysis import find_key_lenght, find_key
from caesar import caesar

def viginere(
    text: str,
    alphabet: Alphabet,
    mode: str,
    key: str = None):
    try:
        if mode == "decrypt" and key:
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
        
        elif mode == "crack" and not key:
            return find_key(find_key_lenght(text))
            
        else:
            raise ValueError("Provide a key when decrypting, or omit it when finding a key")
    
    except ValueError:
        exit()