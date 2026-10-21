from Crypto.Util.number import getPrime, GCD
from pagalbines_funkcijos import string_to_bytes, bytes_to_int, int_to_bytes, bytes_to_string

def rsa_keys(e: int):
    """Generates RSA public and private keys given prime number.
    
    Two prime numbers of 256 bits are generated, then checked for
    equality because they must not match and their GCD with the 
    given prime number must be equal to 1.
    
    Args:
        e: given prime number.
    
    Returns:
        Pairs of public and private keys.
    """
    while True:
        p = getPrime(256)
        comp = GCD(e, p-1)
        if comp != 1:
            continue
        break
    while True:
        q = getPrime(256)
        comp = GCD(e, q-1)
        if comp != 1 or q == p:
            continue
        break
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    
    return (e, n), (d, n)

def name_encryption (name: str, public_key: tuple):
    """Encrypts given name with the given public key.
    
    Name is turned into bytes, bytes are turned to int.
    
    Args:
        name: given name and surname string.
        public_key: consists of a tuple that contains exponent
            and a module *n* that is the product of 2 prime numbers.
    
    Returns:
        cipher text of the encrypted name.
    """
    e, n = public_key
    name = string_to_bytes(name)
    m = bytes_to_int(name)
    c = pow(m, e, n)
    return c

def cipher_decryption (public_key: tuple, cipher: int):
    # e = 3, n = 79982686678088103218738140681847135962460074410801123480380353476204002059633
    # c = 625276106331532937069864335247208594542625
    # C = m ** e % n
    c = cipher
    e, n = public_key
    m = integer_root(c, e)
    check = pow(m, e, n)
    if check == cipher:
        return bytes_to_string(int_to_bytes(m))
    return -1

def integer_root(c: int, e: int) -> int:
    """Returns floor of the e-th root of c using binary search."""
    lo, hi = 0, c
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** e <= c:
            lo = mid
        else:
            hi = mid - 1
    return lo