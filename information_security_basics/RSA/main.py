from constants import NAME_SURNAME, PUBLIC_KEY_3, CIPHER_3, CIPHER_4, PUBLIC_KEY_4, PPRIVATE_KEY, CIPHER_5
from algorithm import rsa_keys, name_encryption, cipher_decryption, cipher_decryption_2, cipher_decryption_3

def main():
    # 1 punktas e = 62653
    print("1.")
    public_key, private_key = rsa_keys(e=62653)
    print(" 3. (e, n):", public_key)
    print(" 4. (d, n):", private_key)
    # 2 punktas vardo užkodavimas viešuoju raktu
    cipher = name_encryption(NAME_SURNAME, public_key)
    print("\n2. Šifras:", cipher)
    # 3 punktas slaptaraščio nulaužimas
    decrypted = cipher_decryption(PUBLIC_KEY_3, CIPHER_3)
    print("\n3. Atšifruotas tekstas:", decrypted)
    # 4 punktas slaptarasčio nulaužimas
    decrypted = cipher_decryption_2(PUBLIC_KEY_4, CIPHER_4)
    print("\n4. Atšifruotas tekstas:", decrypted)
    # 5 punktas slaptarasčio nulaužimas
    decrypted = cipher_decryption_3(PPRIVATE_KEY, CIPHER_5)
    print("\n5. Atšifruotas tekstas:", decrypted)
    
if __name__ == "__main__":
    main()
