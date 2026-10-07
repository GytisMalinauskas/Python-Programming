"""Password cracking using dictionary attack.

Provides a function to crack a password that is hashed with a certain  

Typical usage examples:
    password_cracker("md5", tuple("93ddf33326c602c40d9645befb7c9b15", "ca9adae67c0daf98"))
    password_cracker("bcrypt", "$2b$11$z4viB5e59/nnxmllQ1OWJOMEraKbD92wMfi/xIG.YJgVTyB5a3R2S")
"""

from hashlib import md5, sha256, scrypt
from bcrypt import checkpw
from argon2 import PasswordHasher
from constants import SMALL_FILE_MODE, BIG_FILE_MODE
from argon2.exceptions import VerifyMismatchError
import os

current_folder = os.path.dirname(__file__)

def password_cracker(mode: str, hash_to_crack: set | str):
    """Uses dictionary attack the matching hashes and returns
    
    
    
    Args:
        mode: hashing algorithm to use for the attack.
        hash_to_crack: given hash as a string OR hash and salt as a tuple
            that the functions tries to attack. 
        
    Returns:
        Password as string or -1 if no password hash matches given hash
    """
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
                        hashed_line = scrypt(password=encoded_line, salt=salt.encode(), n=2**16, r=2, p=1).hex()
                        if hashed_line == hash:
                            return line
                if mode == "bcrypt":
                    for line in file:
                        encoded_line = line.rstrip().encode('utf-8')
                        if checkpw(encoded_line, hash.encode()):
                            return line
                if mode == "argon2":
                    ph = PasswordHasher()
                    for line in file:
                        password = line.rstrip()
                        try:
                            if ph.verify(hash, password):
                                return password
                        except VerifyMismatchError:
                            pass
        else:
            raise ValueError()
    except ValueError:
        exit("Consider changing function's password_cracker mode to one of these: \nmd5\nsha256\nscrypt\nbcrypt\nargon2")
    return -1