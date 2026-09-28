"""A module for viginere's cipher testing"""

from viginere import viginere
from constants import TO_DECRYPT, TO_ENCRYPT, LT_ALPHABET, KEY

def main():
    print("\n1 UŽDUOTIS\n", viginere(TO_ENCRYPT, LT_ALPHABET, KEY))
    print("\n2 UŽDUOTIS\n", viginere(TO_DECRYPT, LT_ALPHABET, encrypt=False))
    
if __name__ == "__main__":
    main()
