"""A module for implementing Caesar cipher encryption and decryption"""
# 9th line in txt file
LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"

class Alphabet:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.enumeration = {char : i for char, i in enumerate(alphabet)}
    
    def __len__(self):
        return len(self.alphabet)
    
    def __str__(self):
        return self.alphabet
    
    def __iter__(self):
        for value, index in self.enumeration.items():
            return value, index
    

def main():
    n = 1
    alphabet = Alphabet(LT_ALPHABET)
    print(caesar_cypher(n, alphabet))

def caesar_cypher(n: int,  alphabet: Alphabet):
    # print(n, len(alphabet), alphabet)
    for value, index in alphabet:
        print(value, index)

if __name__ == "__main__":
    main()