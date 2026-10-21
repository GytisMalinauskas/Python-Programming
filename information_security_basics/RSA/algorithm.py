from Crypto.Util.number import getPrime, GCD
from pagalbines_funkcijos import string_to_bytes

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

# 1 punktas e = 62653
print(rsa_keys(e = 62653))

def name_encryption (name: str, public_key: tuple):
    name = string_to_bytes(name)
    