from alphabet import Alphabet

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
        substring_matches.update({substring: matches})
    cleaned_matches = substring_matches.copy()
    for k, v in substring_matches.items():
        if len(v) < 2:
            cleaned_matches.pop(k)
        
find_key_lenght(TO_FIND_KEY, LT_ALPHABET)
