"""Entry point for the dictionary attack exercise.

Demonstrates password cracking of a known hash and salt using different
hashing algorithms like md5, sha256, bcrypt, scrypt and argon2.

Typical usage example:

    python main.py
"""
from cracker import password_cracker
from constants import MD5, SHA_256, ARGON2, BCRYPT, SCRYPT

def main():
    print("md5:", password_cracker("md5", MD5))
    print("sha256:", password_cracker("sha256", SHA_256))
    print("bcrypt:", password_cracker("bcrypt", BCRYPT))
    print("scrypt:", password_cracker("scrypt", SCRYPT))
    print("argon2:", password_cracker("argon2", ARGON2))

if __name__ == "__main__":
    main()