from alphabet import Alphabet

def find_key_lenght(ciphertext: str, alphabet: Alphabet) -> list[int]:
    text_to_process = "".join(char for char in ciphertext.lower() if char in alphabet)
    print(text_to_process)

def find_key(key_lenghts: list[int]) -> str:
    pass

def divide_text_by_lenght():
    pass
