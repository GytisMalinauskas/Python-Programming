from Crypto.Util.number import getPrime, GCD


def rsa():
    p = getPrime(256)
    print(p)
    
rsa()