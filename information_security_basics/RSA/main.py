from constants import NAME_SURNAME
from algorithm import rsa_keys, name_encryption

def main():
    # 1 punktas e = 62653
    public_key, private_key = rsa_keys(e=62653)
    print("1 UŽDUOTIS\nViešasis raktas:", public_key)
    print("Privatusis raktas:", private_key)
    # 2 punktas vardo užkodavimas viešuoju raktu
    cipher = name_encryption(NAME_SURNAME, public_key)
    print("2 UŽDUOTIS\nUžšifruotas vardas ir pavardė:", cipher)

if __name__ == "__main__":
    main()
