from Crypto.Util.number import getPrime, GCD

def rsa():
    # 1 punktas e = 62653
    e = 62653
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
    
    print("viešasis raktas(e,n)", (e, n))
    print("privatusis raktas(d,n)", (d, n))
    
rsa()