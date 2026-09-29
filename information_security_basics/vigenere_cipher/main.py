"""A module for viginere's cipher testing"""

from viginere import viginere
from constants import TO_DECRYPT, TO_FIND_KEY, LT_ALPHABET, KEY

def main():
    print("\n1 ATŠIFRUOTAS TEKSTAS\n", viginere(TO_DECRYPT, LT_ALPHABET, mode="decrypt", key=KEY))
    print("\n2 RASTAS RAKTAS\n", viginere(TO_FIND_KEY, LT_ALPHABET, mode="crack"))
    
if __name__ == "__main__":
    main()
