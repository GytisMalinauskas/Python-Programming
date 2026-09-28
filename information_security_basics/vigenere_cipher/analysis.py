from alphabet import Alphabet

# TODO: remove next line
from constants import TO_FIND_KEY, LT_ALPHABET

def find_key_lenght(ciphertext: str, alphabet: Alphabet, n: int = 3) -> list[int]:
    text_to_process = "".join(char for char in ciphertext.lower() if char in alphabet)
    for i in range(len(text_to_process) - n + 1):
        substring = text_to_process[i:i+n]
        for j in range(i, len(text_to_process)):
            print (i, j)
def find_key(key_lenghts: list[int]) -> str:
    pass

find_key_lenght(TO_FIND_KEY, LT_ALPHABET)
