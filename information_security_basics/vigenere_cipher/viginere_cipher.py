def caesar_cipher(
    text: str,
    alphabet: Alphabet,
    n: int = 3,
    encrypt: bool = True,
) -> str:
    """Encrypt or decrypt text using the Caesar cipher.

    Each character that belongs to the alphabet is shifted by n positions.
    Characters not in the alphabet (spaces, punctuation, digits) are kept
    as-is. Input is lowercased and stripped of leading/trailing whitespace
    before processing.

    Parameters:
        text (str): The string to encrypt or decrypt.
        alphabet (Alphabet): The Alphabet instance that defines the character set and
            their positions.
        n (int): The number of positions to shift each character. Must be a
            non-negative integer; values larger than len(alphabet) wrap
            around automatically. Defaults to 3.
        encrypt (bool): If True (default), shift forward (encrypt). If False,
            shift backward (decrypt).

    Returns:
        output (str): The processed string with the same length as the (lowercased,
            stripped) input.

    Example::

        alpha = Alphabet("abcde")
        caesar_cipher("ace", alpha, n=1)              # → "bda"
        caesar_cipher("bda", alpha, n=1, encrypt=False)  # → "ace"
    """
    text = text.lower().strip()
    direction = 1 if encrypt else -1
    result = []
    for char in text:
        if char not in alphabet:
            result.append(char)
            continue
        new_index = (alphabet[char] + n * direction) % len(alphabet)
        result.append(alphabet[new_index])
    return "".join(result)

def viginere_cipher(alphabet: str):
    alphabet_matrix = matrix(alphabet)
    # TODO: Find key lenght
    # TODO: Divide text by key length
    # TODO: Find the Ceaser's shift
    pass

def find_key_lenght():
    pass

def divide_text_by_lenght():
    pass

def find_key():
    pass

def matrix(alphabet: str):
    letters = []
    for char in alphabet:
        letters.append(char)
    alphabet_matrix = []
    for _ in range(len(alphabet)):
        alphabet_matrix.append(letters.copy())
        value_to_move_back = letters.pop(0)
        letters.append(value_to_move_back)
    return alphabet_matrix

def main():
    print(viginere_cipher(LT_ALPHABET))
    
if __name__ == "__main__":
    main()
