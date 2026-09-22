"""A module for implementing Caesar cipher encryption and decryption"""

LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
TO_ENCRYPT = "9. Kalbos – vežimais, o naudos – už grašį. 19"
TO_DECRYPT = "9. Fp bfbcyfl nvprl fpcfkv fp įnvprl."

class Alphabet:
    """Alphabet class used by caesars_cypher function.

    Used to instantiate instance of Alphabet.
    """
    def __init__(self, alphabet):
        """Initializes an instance.
        
        Alphabet dictionary maps characters to indexes. 
        """
        self.alphabet = alphabet
        self._char_to_index = {char : i for i, char in enumerate(alphabet)}
        self._index_to_char = {i : char for i, char in enumerate(alphabet)}
    
    def __len__(self):
        return len(self.alphabet)
    
    def __str__(self):
        return self.alphabet
    
    def __getitem__(self, key):
        return list(self.alphabet_dictionary._char_to_index())[list(self.alphabet_dictionary._char_to_index()).index(key)]
    
    def __iter__(self):
        """Yields value and index from initialized dictionary when iterating"""
        for value, index in self.alphabet_dictionary._char_to_index():
            yield value, index
    

def caesar_cypher(text: str, alphabet: Alphabet, n: int = 3, encrypt: bool = True):
    """
        Encrypts / Decripts a text with caesar's cypher.
        @param text is a string to ecrypt/decript with caesar's cypher
        @param n is the shift index.
        @param alphabet takes Alphabet class object
        @param encrypt used to enable encryption mode otherwise decryption mode is enabled
    """
    text = text.lower().strip()
    outcome = ""
    if encrypt:
        for char in text:
            if not char in str(alphabet):
                outcome += char
                continue
            for value, index in alphabet:
                if char == value:
                    new_index = (index + n) % len(alphabet)
                    new_value = alphabet[new_index]
                    outcome += new_value
                    break
    else:
        for char in text:
            if not char in str(alphabet):
                outcome += char
                continue
            for value, index in alphabet:
                if char == value:
                    new_index = (index - n) % len(alphabet)
                    new_value = alphabet[new_index]
                    outcome += new_value
                    break
    return outcome

def main():
    alphabet = Alphabet(LT_ALPHABET)
    print(caesar_cypher(TO_ENCRYPT, alphabet))
    print(caesar_cypher(TO_DECRYPT, alphabet, n = 29, encrypt = False))


if __name__ == "__main__":
    main()