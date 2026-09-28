from alphabet import Alphabet
from math import gcd
# TODO: remove next line
from constants import TO_FIND_KEY, LT_ALPHABET

def find_key(key_lenghts: list[int]) -> str:
    pass

def find_key_lenght(ciphertext: str, alphabet: Alphabet, n: int = 3) -> list[int]:
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
    print(sorted(substring_matches.items(), key=lambda item:len(item[1]), reverse=True))

find_key_lenght(TO_FIND_KEY, LT_ALPHABET)
