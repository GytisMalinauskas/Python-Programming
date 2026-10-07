from hashlib import md5, sha256, scrypt
from bcrypt import checkpw
from argon2 import PasswordHasher
from constants import SMALL_FILE_MODE, BIG_FILE_MODE
import os

current_folder = os.path.dirname(__file__)

def password_cracker(mode: str, hash_to_crack: set | str):
    mode = mode.lower().strip()
    try:
        if mode in BIG_FILE_MODE:
            hash, salt = hash_to_crack
            file_path = os.path.join(current_folder, "rockyou.txt")
            with open(file_path, 'r', encoding="latin-1") as file:
                if mode == "md5":
                    for line in file:
                        salted_line = (line.rstrip() + salt).encode()
                        hashed_line = md5(salted_line).hexdigest()
                        if hashed_line == hash:
                            return line
                if mode == "sha256":
                    for line in file:
                        salted_line = (line.rstrip() + salt).encode()
                        hashed_line = sha256(salted_line).hexdigest()
                        if hashed_line == hash:
                            return line
        elif mode in SMALL_FILE_MODE:
            if isinstance(hash_to_crack, tuple):
                hash, salt = hash_to_crack
            else:
                hash = hash_to_crack
            file_path = os.path.join(current_folder, "rockyou_1000.txt")
            with open(file_path, 'r', encoding="latin-1") as file:
                if mode == "scrypt":
                    for line in file:
                        encoded_line = line.rstrip().encode()
                        hashed_line = scrypt(password=encoded_line, salt=salt, n=2**16, r=2, p=1).hexdigest()
                        if hashed_line == hash:
                            return line
                if mode == "bcrypt":
                    return 1
                if mode == "argon2":
                    return 2
        else:
            raise ValueError()
    except ValueError:
        exit("Consider changing function's password_cracker mode to one of these: \nmd5\nsha256\nscrypt\nbcrypt\nargon2")
