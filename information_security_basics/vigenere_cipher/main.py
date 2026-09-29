"""Entry point for the Vigenère cipher exercise.

Demonstrates decryption with a known key and automatic key recovery
using Kasiski examination with Friedman's index of coincidence.

Typical usage example:

  python main.py
"""

from constants import KEY, LT_ALPHABET, TO_DECRYPT, TO_FIND_KEY
from viginere import viginere

def main():
    print("\n1 ATŠIFRUOTAS TEKSTAS\n", viginere(TO_DECRYPT, LT_ALPHABET, mode="decrypt", key=KEY))
    print("\n2 RASTAS RAKTAS\n", viginere(TO_FIND_KEY, LT_ALPHABET, mode="crack"))
    
if __name__ == "__main__":
    main()
