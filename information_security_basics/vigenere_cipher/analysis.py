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
        if substring in substring_matches.keys():
            continue
        matches = 0
        for j in range(i+3, len(text_to_process)):
            substring2 = text_to_process[j:j+n]
            if substring == substring2:
                matches += 1
        substring_matches.update({substring: matches})
    print(sorted(substring_matches.items(), key=lambda item: item[1], reverse=True))


find_key_lenght(TO_FIND_KEY, LT_ALPHABET)
