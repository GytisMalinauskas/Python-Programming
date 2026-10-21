from Crypto.Util.number import getPrime, GCD
from pagalbines_funkcijos import string_to_bytes, bytes_to_int, int_to_bytes, bytes_to_string, integer_root, byte_length
from sympy import factorint

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
    print("p reikšmė:", p)
    print("q reikšmė:", q)
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    
    return (e, n), (d, n)

def name_encryption(name: str, public_key: tuple):
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

def cipher_decryption(public_key: tuple, cipher: int):
    """Decrypts given cipher using the given public key.
    
    Given mᵉ < n, then c = n = mᵉ, meaning that you can
    calculate m like this: m = c^(1/e) but it returs a float which
    is inaccurate. Function `integer_root` finds the e-th root
    of an integer using binary search algoritm.
    
    Args: 
        public_key: consists of a tuple that contains exponent
            and a module *n* that is the product of 2 prime numbers.
        cipher: cipher text to decrypt.
    Returns:
        A decrypted cipher text string or -1 if something is wrong.
    """
    e, n = public_key
    m = integer_root(cipher, e)
    check = pow(m, e, n)
    if check == cipher:
        return bytes_to_string(int_to_bytes(m))
    return -1

def cipher_decryption_2(public_key: tuple, cipher: int):
    """Decrypts given cipher using the given public key.
    
    Given that n of the public_key is 40 bits, means that p and q
    can be factored out.
    
    Args: 
    public_key: consists of a tuple that contains exponent
        and a module *n* that is the product of 2 prime numbers.
    cipher: cipher text to decrypt
    
    Returns:
        A decrypted cipher text string or -1 if something is wrong.
    """
    
    e, n = public_key
    p, q = factorint(n).keys()
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(cipher, d, n)
    check = pow(m, e, n)
    if check == cipher:
        return bytes_to_string(int_to_bytes(m))
    return -1

def cipher_decryption_3(private_key: tuple, cipher: int):
    d, n = private_key
    k = byte_length(n)
    
    m = pow(cipher, d, n)
    em = int_to_bytes(m)
    
    print(em)
    if em[0] != 0x00 or em[1] != 0x02:
        return None
    return -1