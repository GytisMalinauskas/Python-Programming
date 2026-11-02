from aes_cipher import aes_decrypt, aes_encrypt
from constants import KEY, TEXT

def main():
    print("1. Dešifruotas tekstas:", aes_decrypt(TEXT, KEY))
    print("2. Užšifruota pavardė:", aes_encrypt("Malinauskas", KEY) )
    
if __name__ == "__main__":
    main()