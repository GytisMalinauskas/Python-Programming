"""Kasiski examination and frequency analysis for Vigenère key recovery.

Provides functions to determine the key length of a Vigenère-encrypted
ciphertext using Kasiski examination cross-checked with Friedman's index
of coincidence, and to recover the key itself using Caesar cipher frequency
analysis.

Typical usage example:

    key_length = find_key_length(ciphertext, alphabet)
    key = find_key(ciphertext, alphabet, key_length)
"""

from alphabet import Alphabet
from math import gcd
from functools import reduce
from collections import Counter
from caesar import crack_caesar
from constants import LT_SIMILARITY_PROBABILITY, LT_TEXT_OVERLAP_INDEX

def find_key(ciphertext:str, alphabet: Alphabet, key_lenght: int) -> str:
    """Recovers the Vigenère key from ciphertext given the key length.

    Splits the ciphertext into key_length independent Caesar cipher streams,
    then applies frequency analysis to each stream to determine its shift,
    assembling the shifts into the key.

    Args:
        ciphertext: The encrypted text to analyse.
        alphabet: The Alphabet instance defining the character set.
        key_length: The length of the Vigenère key to recover.

    Returns:
        The recovered key as a plaintext string.
    """
    divide_to_caesar_ciphers = {}
    caesar_index = 0
    text_to_process = text_to_process_func(ciphertext, alphabet)
    for char in text_to_process:
        get_string = divide_to_caesar_ciphers.get(caesar_index, "")
        divide_to_caesar_ciphers.update({caesar_index: "".join([get_string, char])})
        caesar_index = (caesar_index + 1) % key_lenght
    shifts = []
    for caesar_index in divide_to_caesar_ciphers.values():
        shifts.append(alphabet[crack_caesar(caesar_index, alphabet)])
    return "".join(shifts)

def find_key_lenght(ciphertext: str, alphabet: Alphabet, n: int = 2) -> int:
    """Determines the most likely Vigenère key length using Kasiski examination.

    Finds repeated substrings of length n in the ciphertext and computes the
    GCD of the distances between them. Candidates are then ranked by how
    closely they match the key length estimate from Friedman's index of
    coincidence, and the best candidate is returned.

    Args:
        ciphertext: The encrypted text to analyse.
        alphabet: The Alphabet instance defining the character set.
        n: Minimum length of repeated substrings to search for. Defaults to 2.

    Returns:
        The most likely key length as a positive integer.
    """
    text_to_process = text_to_process_func(ciphertext, alphabet)
    substring_matches = {}
    for i in range(len(text_to_process) - n + 1):
        substring = text_to_process[i:i+n]
        if substring in substring_matches:
            continue
        matches = []
        matches.append(i)
        for j in range(i+n, len(text_to_process)):
            substring2 = text_to_process[j:j+n]
            if substring == substring2:
                matches.append(j)
        distances = [b - a for a, b in zip(matches, matches[1:])]
        if len(distances) == 0:
            continue
        substring_matches[substring] = distances
    gcd_matches = Counter()
    for distance_list in substring_matches.values():
        gcd_of_distance_list = reduce(gcd, distance_list)
        gcd_matches[gcd_of_distance_list] += 1
    top_10 = [key_length for key_length, _ in sorted(gcd_matches.items(), key=lambda item:item[1], reverse=True)[:10] if key_length > 1]
    friedmans_upper = 0
    for char in str(alphabet):
        repeats = text_to_process.count(char)
        friedmans_upper += repeats * (repeats - 1)
    friedmans_lower = len(text_to_process) * (len(text_to_process) - 1)
    friedmans_index = friedmans_upper / friedmans_lower
    viginere_key_lenght_aprox = (LT_TEXT_OVERLAP_INDEX - LT_SIMILARITY_PROBABILITY) / (friedmans_index -LT_SIMILARITY_PROBABILITY) 
    top_10_ranked = {}
    for lenght in top_10:
        difference = abs(lenght - viginere_key_lenght_aprox)
        top_10_ranked[lenght] = difference
    return sorted(top_10_ranked.items(), key=lambda item:item[1], reverse=False)[0][0]

def text_to_process_func(ciphertext: str, alphabet: Alphabet) -> str:
    """Removes non-alphabet characters and lowercases the ciphertext.

    Args:
        ciphertext: The text to clean.
        alphabet: The Alphabet instance defining valid characters.

    Returns:
        A lowercased string containing only characters present in alphabet.
    """
    return "".join(char for char in ciphertext.lower() if char in alphabet)
