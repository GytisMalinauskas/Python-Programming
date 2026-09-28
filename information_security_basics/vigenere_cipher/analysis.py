from alphabet import Alphabet

# TODO: remove next line
from constants import TO_FIND_KEY, LT_ALPHABET

def find_key(key_lenghts: list[int]) -> str:
    pass

def find_key_lenght(ciphertext: str, alphabet: Alphabet, n: int = 3) -> list[int]:
    text_to_process = "".join(char for char in ciphertext.lower() if char in alphabet)
    for i in range(len(text_to_process) - n + 1):
        substring = text_to_process[i:i+n]
        for j in range(i+3, len(text_to_process)):
            substring2 = text_to_process[j:j+n]
            print(substring, substring2)
            


find_key_lenght(TO_FIND_KEY, LT_ALPHABET)
