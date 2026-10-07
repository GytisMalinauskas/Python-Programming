from hashlib import md5, sha256, scrypt
from bcrypt import checkpw
from argon2 import PasswordHasher
from constants import SMALL_FILE_MODE, BIG_FILE_MODE 

def password_cracker(mode: str, hash: str, salt: str):
    mode = mode.lower().strip()
    try:
        if mode in BIG_FILE_MODE:
            ...
        elif mode in SMALL_FILE_MODE:
            ...
        else:
            raise ValueError
        
    except ValueError:
        exit("\nmd5\nsha256\nscrypt\nbcrypt\nargon2")