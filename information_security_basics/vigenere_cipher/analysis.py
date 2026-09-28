from alphabet import Alphabet
from math import gcd
from functools import reduce
from collections import Counter

# TODO: remove next line
from constants import TO_FIND_KEY, LT_ALPHABET, LT_SIMILARITY_PROBABILITY, LT_TEXT_OVERLAP_INDEX

def find_key(ciphertext:str, alphabet: Alphabet, key_lenght: int) -> str:
    divide_to_caesar_ciphers = {}
    caesar_index = 0
    text_to_process = text_to_process_func(ciphertext, alphabet)
    for char in text_to_process:
        get_string = divide_to_caesar_ciphers.get(caesar_index, "")
        divide_to_caesar_ciphers.update({caesar_index: "".join([get_string, char])})
        caesar_index = (caesar_index + 1) % key_lenght
    

def find_key_lenght(ciphertext: str, alphabet: Alphabet, n: int = 2) -> int:
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
    return "".join(char for char in ciphertext.lower() if char in alphabet)

print(find_key(TO_FIND_KEY, alphabet=LT_ALPHABET, key_lenght=find_key_lenght(TO_FIND_KEY, LT_ALPHABET)))
