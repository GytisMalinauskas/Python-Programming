"""A module for the implementation of Caesar's cipher encryption and decryption."""
from alphabet import Alphabet

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

    Args:
        text: The string to encrypt or decrypt.
        alphabet: The Alphabet instance that defines the character set and
            their positions.
        n: The number of positions to shift each character. Must be a
            non-negative integer; values larger than len(alphabet) wrap
            around automatically. Defaults to 3.
        encrypt: If True (default), shift forward (encrypt). If False,
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