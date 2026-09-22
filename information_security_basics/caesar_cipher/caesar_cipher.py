"""A module for implementing Caesar cipher encryption and decryption"""

LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
TO_ENCRYPT = "9. Kalbos – vežimais, o naudos – už grašį. 19"
TO_DECRYPT = "9. Fp bfbcyfl nvprl fpcfkv fp įnvprl."

class Alphabet:
    """Alphabet class used by caesars_cipher function.

    Used to instantiate instance of Alphabet.
    """
    def __init__(self, alphabet):
        """Initializes an instance.
        
        """
        self._alphabet = alphabet
        self._char_to_index = {char : i for i, char in enumerate(alphabet)}
        self._index_to_char = {i : char for i, char in enumerate(alphabet)}
    
    def __len__(self):
        return len(self._alphabet)
    
    def __str__(self):
        return self._alphabet
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._index_to_char[key]
        if isinstance(key, str):
            return self._char_to_index[key]    
    
    def __iter__(self):
        """Yields value and index from initialized dictionary when iterating"""
        for value, index in self._char_to_index.items():
            yield value, index
    

def caesar_cipher(text: str, alphabet: Alphabet, n: int = 3, encrypt: bool = True):
    """
        Encrypts / Decripts a text with caesar's cipher.
        @param text is a string to ecrypt/decript with caesar's cipher
        @param n is the shift index.
        @param alphabet takes Alphabet class object
        @param encrypt used to enable encryption mode otherwise decryption mode is enabled
    """
    text = text.lower().strip()
    outcome = []
    direction = 1 if encrypt else -1
    for char in text:
        if not char in str(alphabet):
            outcome.append(char)
            continue
        new_index = (alphabet[char] + n * direction) % len(alphabet)
        new_char = alphabet[new_index]
        outcome.append(new_char)
    return "".join(outcome)

def main():
    alphabet = Alphabet(LT_ALPHABET)
    print(caesar_cipher(TO_ENCRYPT, alphabet))
    print(caesar_cipher(TO_DECRYPT, alphabet, n = 29, encrypt = False))


if __name__ == "__main__":
    main()