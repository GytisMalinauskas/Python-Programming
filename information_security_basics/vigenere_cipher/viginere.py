"""Vigenère cipher decryption and key discovery.

Provides a single entry point, viginere(), that either decrypts a ciphertext
using a known key, or attempts to recover the key automatically using Kasiski
examination combined with Caesar cipher frequency analysis.

Typical usage example:

  plaintext = viginere(ciphertext, alphabet, mode="decrypt", key="minija")
  found_key = viginere(ciphertext, alphabet, mode="crack")
"""

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
                if char.lower() not in alphabet:
                    encrypted_chars.append(char)
                    continue
                is_upper = char != char.lower()
                keychar_index = alphabet[key[key_index]]
                if is_upper:
                    encrypted_char = caesar(char.lower(), alphabet, keychar_index, encrypt=False).upper()
                else:
                    encrypted_char = caesar(char, alphabet, keychar_index, encrypt=False)
                encrypted_chars.append(encrypted_char)
                key_index = (key_index + 1) % len(key)
            return "".join(encrypted_chars)
        
        elif mode == "crack" and not key:
            return find_key(text, alphabet, find_key_lenght(text, alphabet))
            
        else:
            raise ValueError("Provide a key when decrypting, or omit it when finding a key")
    
    except ValueError:
        exit()