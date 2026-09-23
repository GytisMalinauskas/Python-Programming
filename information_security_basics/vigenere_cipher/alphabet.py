"""A module for Alphabet class implementation.

Alphabet class is used to instantiate an alphabet specifically that is used 
by the Caesar's cipher.

    Example::
        alpha = Alphabet("abcde")
        alpha["c"]   # → 2  (char to index)
        alpha[2]     # → "c"  (index to char)
        "c" in alpha # → True
"""

class Alphabet:
    """A bidirectional mapping between characters and their positions.

    Wraps a string alphabet so that caesar_cipher can look up a character's
    index and look up the character at a given index in O(1) time.

    Attributes: 
        alphabet: A string of Unique characters that define the cipher's
            alphabet. The position of each character determines its index.
        char_to_index: A dictionary, that maps character to index.
        index_to_char: A dictionary, that maps index to character.
    """

    def __init__(self, alphabet: str) -> None:
        """Initializes the instance of the alphabet.
        
        Args:
            alphabet: defines a string that is passed when initiating.
        """
        
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

        Parameters:
            key (int | str): A character (str) to look up its index, or an integer
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
