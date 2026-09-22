"""A module for implementing Caesar cipher encryption and decryption.

The Caesar cipher shifts each letter in a text forward (encryption) or
backward (decryption) by a fixed number of positions within an alphabet.
Non-alphabet characters (digits, punctuation, spaces) are passed through
unchanged.

Example usage::

    alphabet = Alphabet(LT_ALPHABET)
    encrypted = caesar_cipher("labas", alphabet, n=3)
    decrypted = caesar_cipher(encrypted, alphabet, n=3, encrypt=False)
    shift, score, plaintext = crack_caesar(encrypted, alphabet)
"""

LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
TO_ENCRYPT = "9. Kalbos – vežimais, o naudos – už grašį. 19"
TO_DECRYPT = "9. Fp bfbcyfl nvprl fpcfkv fp įnvprl."

# Letters used to score decryption candidates during key cracking.
# These are the most frequent letters in Lithuanian text; a candidate
# that contains many of them is more likely to be valid plaintext.
COMMON_LT_LETTERS = "iasore"


class Alphabet:
    """A bidirectional mapping between characters and their positions.

    Wraps a string alphabet so that caesar_cipher can look up a character's
    index and look up the character at a given index in O(1) time.

    Attributes
    ----------
        alphabet : str 
            A string of unique characters that define the cipher's
            alphabet. The position of each character determines its index.

    Example::

        alpha = Alphabet("abcde")
        alpha["c"]   # → 2  (char to index)
        alpha[2]     # → "c"  (index to char)
        "c" in alpha # → True
    """

    def __init__(self, alphabet: str) -> None:
        self._alphabet = alphabet
        # Two dicts instead of one let both lookup directions run in O(1).
        self._char_to_index = {char: i for i, char in enumerate(alphabet)}
        self._index_to_char = {i: char for i, char in enumerate(alphabet)}

    def __len__(self) -> int:
        return len(self._alphabet)

    def __str__(self) -> str:
        return self._alphabet

    def __contains__(self, char: str) -> bool:
        return char in self._char_to_index

    def __getitem__(self, key: int | str) -> str | int:
        """Return the index for a character, or the character at an index.

        Args:
            key: A character (str) to look up its index, or an integer
                index to look up the corresponding character.

        Returns:
            The integer index when key is a str, or the character when
            key is an int.

        Raises:
            KeyError: If the character is not in the alphabet, or the
                index is out of range.
            TypeError: If key is neither str nor int.
        """
        if isinstance(key, int):
            return self._index_to_char[key]
        if isinstance(key, str):
            return self._char_to_index[key]
        raise TypeError(f"Key must be str or int, got {type(key).__name__!r}")

    def __iter__(self):
        """Yield (character, index) pairs in definition order."""
        for value, index in self._char_to_index.items():
            yield value, index


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
        The processed string with the same length as the (lowercased,
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


def crack_caesar(
    ciphertext: str,
    alphabet: Alphabet,
) -> tuple[int, float, str]:
    """Find the most likely Caesar cipher shift by frequency analysis.

    Tries every possible shift (0 to len(alphabet) - 1), decrypts the
    ciphertext with each one, and scores the result by counting how many
    of the decrypted letters appear in COMMON_LT_LETTERS. The candidate
    with the highest score is returned.

    Args:
        ciphertext: The encrypted text whose shift is unknown.
        alphabet: The Alphabet instance used to define valid letters.

    Returns:
        A tuple of (shift, score, plaintext) for the best candidate, where
        shift is the int key, score is a float in [0.0, 1.0] representing
        the fraction of letters that matched common letters, and plaintext
        is the decrypted string.

    Raises:
        ZeroDivisionError: If ciphertext contains no alphabet characters
            (e.g. it is entirely punctuation or digits).

    Example::

        alpha = Alphabet(LT_ALPHABET)
        shift, score, text = crack_caesar("Fp bfbcyfl", alpha)
    """
    results = []
    for shift in range(len(alphabet)):
        candidate = caesar_cipher(ciphertext, alphabet, n=shift, encrypt=False)
        letters = [c for c in candidate if c in alphabet]
        score = sum(1 for c in letters if c in COMMON_LT_LETTERS) / len(letters)
        results.append((shift, score, candidate))
    results.sort(key=lambda x: -x[1])
    return results[0]


def main() -> None:
    alphabet = Alphabet(LT_ALPHABET)
    print(caesar_cipher(TO_ENCRYPT, alphabet))
    print(crack_caesar(TO_DECRYPT, alphabet))


if __name__ == "__main__":
    main()