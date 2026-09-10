"""A module for implementing Caesar cipher encryption and decryption"""
# 
ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
ALPHABET_DICT = {char: i for char, i in enumerate(ALPHABET)}

def main():
    caesar_cypher()

def caesar_cypher(n: int, alphabet_length: int, alphabet_dict: dict):
    pass