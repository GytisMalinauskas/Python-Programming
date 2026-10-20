from Crypto.Util.number import getPrime, GCD

def rsa():
    while True:
        p = getPrime(256)
        q = getPrime(256)
        # 1 punktas e = 62653
        e = 62653
        if GCD(e, p-1) != 1 or GCD(e, q-1) != 1 and q != p:
            continue
    
rsa()