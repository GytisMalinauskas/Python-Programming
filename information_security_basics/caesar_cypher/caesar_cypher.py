"""A module for implementing Caesar cipher encryption and decryption"""
# 
LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"

def main():
    n = 1
    print(caesar_cypher(n, LT_ALPHABET))

def caesar_cypher(n: int,  alphabet: str):
    alphabet_lenght = len(alphabet)
    aplhabet_dict = {char: i for char, i in enumerate(LT_ALPHABET)}
    return str