"""A module for implementing Caesar cipher encryption and decryption"""
# 
LT_ALPHABET = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
LT_ALPHABET_DICT = {char: i for char, i in enumerate(LT_ALPHABET)}

def main():
    caesar_cypher()

def caesar_cypher(n: int, alphabet_length: int, alphabet_dict: dict):
    pass