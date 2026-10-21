from constants import NAME_SURNAME, PUBLIC_KEY_3, CIPHER_3, CIPHER_4, PUBLIC_KEY_4, PPRIVATE_KEY, CIPHER_5
from algorithm import rsa_keys, name_encryption, cipher_decryption, cipher_decryption_2, cipher_decryption_3

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
    decrypted = cipher_decryption_2(PUBLIC_KEY_4, CIPHER_4)
    print("\n4 UŽDUOTIS\nAtšifruotas tekstas:", decrypted)
    # 5 punktas slaptarasčio nulaužimas
    decrypted = cipher_decryption_3(PPRIVATE_KEY, CIPHER_5)
    print("\n5 UŽDUOTIS\nAtšifruotas tekstas:", decrypted)
    
if __name__ == "__main__":
    main()
