from constants import NAME_SURNAME, PUBLIC_KEY_3, CIPHER_3
from algorithm import rsa_keys, name_encryption, cipher_decryption

def main():
    # 1 punktas e = 62653
    print("1 UŽDUOTIS")
    public_key, private_key = rsa_keys(e=62653)
    print("(e, n):", public_key)
    print("(d, n):", private_key)
    # 2 punktas vardo užkodavimas viešuoju raktu
    cipher = name_encryption(NAME_SURNAME, public_key)
    print("\n2 UŽDUOTIS\nŠifras:", cipher)
    # 3 punktas slaptaraščio nulaužimas
    decrypted = cipher_decryption(PUBLIC_KEY_3, CIPHER_3)
    print("\n3 UŽDUOTIS\nAtšifruotas tekstas:", decrypted)
    # 4 punktas slaptarasčio nulaužimas
    
if __name__ == "__main__":
    main()
