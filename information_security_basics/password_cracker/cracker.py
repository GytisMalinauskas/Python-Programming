from hashlib import md5, sha256, scrypt
from bcrypt import checkpw
from argon2 import PasswordHasher
from constants import SMALL_FILE_MODE, BIG_FILE_MODE 

def password_cracker(mode: str, hash_to_crack: set | str):
    mode = mode.lower().strip()
    try:
        if mode in BIG_FILE_MODE:
            hash, salt = hash_to_crack
            if mode == "md5":
                return 0
            if mode == "sha256":
                return 1
        elif mode in SMALL_FILE_MODE:
            if isinstance(hash_to_crack, set):
                hash, salt = hash_to_crack
            else:
                hash = hash_to_crack
            if mode == "scrypt":
                return 0
            if mode == "bcrypt":
                return 1
            if mode == "argon2":
                return 2
        else:
            raise ValueError()
    except ValueError:
        exit("Consider changing function's password_cracker mode to one of these: \nmd5\nsha256\nscrypt\nbcrypt\nargon2")
