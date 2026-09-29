"""A module for the implementation of Caesar's cipher encryption and decryption.

Typical usage example:
    alpha = Alphabet("abcde")
    caesar("ace", alpha, n=1)              # → "bda"
    caesar("bda", alpha, n=1, encrypt=False)  # → "ace"
    
    cipher_text = "Fp bfbcyfl"
    shift = crack_caesar(ciphertext , alpha)
"""
from alphabet import Alphabet
from constants import LT_COMMON_LETTERS

def caesar(
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
        output: The processed string with the same length as the (lowercased,
            stripped) input.
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

def crack_caesar(
    ciphertext: str,
    alphabet: Alphabet,
) -> tuple[int, float, str]:
    """Find the most likely Caesar cipher shift by frequency analysis.

    Tries every possible shift (0 to len(alphabet) - 1), decrypts the
    ciphertext with each one, and scores the result by counting how many
    of the decrypted letters appear in COMMON_LT_LETTERS. The candidate
    with the highest score is returned.

    Parameters:
        ciphertext (str): The encrypted text whose shift is unknown.
        alphabet (Alphabet): The Alphabet instance used to define valid letters.

    Returns:
        output (tuple(int, float, str)): A tuple of (shift, score, plaintext) 
            for the best candidate, where shift is the int key, score is a float 
            in [0.0, 1.0] representing the fraction of letters that matched 
            common letters, and plaintext is the decrypted string.

    Raises:
        ZeroDivisionError: If ciphertext contains no alphabet characters
            (e.g. it is entirely punctuation or digits).
    """
    results = []
    for shift in range(len(alphabet)):
        candidate = caesar(ciphertext, alphabet, n=shift, encrypt=False)
        letters = [c for c in candidate if c in alphabet]
        score = sum(1 for c in letters if c in LT_COMMON_LETTERS) / len(letters)
        results.append((shift, score, candidate))
    results.sort(key=lambda x: -x[1])
    return results[0][0]