from Crypto.Util.number import getPrime, GCD

def rsa(e: int):
    """Generates RSA public and private keys given prime number.
    
    
    
    Returns:
        pairs of public and private keys
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
print(rsa(e = 62653))