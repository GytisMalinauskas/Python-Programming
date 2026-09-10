"""A module for implementing Caesar cipher encryption and decryption"""
# 
LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
LT_ALPHABET_DICT = {char: i for char, i in enumerate(LT_ALPHABET)}

def main():
    n = 1
    print(caesar_cypher(n, len(LT_ALPHABET), LT_ALPHABET_DICT))

def caesar_cypher(n: int, alphabet_length: int, alphabet: str):
    
    return str