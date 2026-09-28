from alphabet import Alphabet
from math import gcd
from functools import reduce
from collections import Counter

# TODO: remove next line
from constants import TO_FIND_KEY, LT_ALPHABET, LT_SIMILARITY_PROBABILITY, LT_TEXT_OVERLAP_INDEX

def find_key(key_lenghts: list[int]) -> str:
    pass

def find_key_lenght(ciphertext: str, alphabet: Alphabet, n: int = 2) -> int:
    text_to_process = "".join(char for char in ciphertext.lower() if char in alphabet)
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
    for char in str(alphabet):
        text_to_process.count(char)
print(find_key_lenght(TO_FIND_KEY, LT_ALPHABET))
