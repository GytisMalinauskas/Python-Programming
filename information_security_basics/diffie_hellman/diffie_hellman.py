from math import isqrt
import sympy

def secret_generation(g, p, a, b):
    A = pow(g,a,p)
    B = pow(g,b,p)
    s1 = pow(B,a,p)
    s2 = pow(A,b,p)
    assert s1 == s2, "Wrong secrets"
    
    return s1

def baby_step_giant_step(g, p, x):
    m = isqrt(p - 1) + 1
    values = {}
    
    for j in range(m):
        v = pow(g, m * j, p)
        values[v] = j
        
    for i in range(m):
        v2 = (pow(g, -i, p) * x) % p
        if v2 in values:
            j = values[v2]
            return (m * j + 1) % (p - 1)
        
def generate_prime(bits, g):
    while True:
        q = sympy.randprime(pow(2, 98), pow(2, 99) - 1)
        p = 2 * q + 1
        if sympy.isprime(p):
            r1 = pow(2, q, p)
            r2 = pow(2, g, p)
            if r1 != 1 and r2 != 1:
                return p