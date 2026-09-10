"""A module for implementing Caesar cipher encryption and decryption"""
# 9th line in txt file
LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"

class Alphabet:
    """alphabet class used by caesars_cypher function.

    Used to instantiate instance of Alphabet.
    """
    def __init__(self, alphabet):
        """Initializes an instance.
        
        Alphabet dictionary maps characters to indexes. 
        """
        self.alphabet = alphabet
        self.alphabet_dictionary = {char : i for i, char in enumerate(alphabet)}
    
    def __len__(self):
        """"""
        return len(self.alphabet)
    
    def __str__(self):
        return self.alphabet
    
    def __iter__(self):
        for value, index in self.alphabet_dictionary.items():
            yield value, index
    

def main():
    n = 1
    alphabet = Alphabet(LT_ALPHABET)
    print(caesar_cypher(n, alphabet))

def caesar_cypher(n: int, alphabet: Alphabet, encrypt: bool = True):
    """
        Encrypts/Decripts a text with caesar's cypher.
        @param n is the shift index.
        @param alphabet takes Alphabet class object
        @param encrypt used to enable encryption mode otherwise decryption mode is enabled
    """
    # print(n, len(alphabet), alphabet)
    # for value, index in alphabet:
    #     print(value, index)
    pass

if __name__ == "__main__":
    main()