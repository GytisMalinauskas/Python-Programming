from math import sqrt
import sympy

def secret_generation(g, p, a, b):
    A = g ** a % p
    B = g ** b % p
    s1 = B ** a % p
    s2 = A ** b % p
    assert s1 == s2, "Wrong secrets"
    
    return s1