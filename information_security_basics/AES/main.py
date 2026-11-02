from aes_cipher import aes_encrypt
from constants import KEY, TEXT

def main():
    print("1. Dešifruotas tekstas:", aes_encrypt(TEXT, KEY))
    print("2. Užšifruota pavardė:")
    
if __name__ == "__main__":
    main()