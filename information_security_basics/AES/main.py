from aes_cipher import aes_decrypt, aes_encrypt
from constants import KEY, TEXT

def main():
    print("1. Dešifruotas tekstas:", aes_decrypt(TEXT, KEY))
    print("2.1 Užšifruota pavardė:", aes_encrypt("Malinauskas", KEY))
    print("2.2 Šifravimui naudotas raktas:", KEY)
    
if __name__ == "__main__":
    main()