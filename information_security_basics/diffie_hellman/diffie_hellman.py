from math import sqrt
import sympy

def secret_generation(g, p, a, b):
    A = pow(g,a,p)
    B = pow(g,b,p)
    s1 = pow(B,a,p)
    s2 = pow(A,b,p)
    assert s1 == s2, "Wrong secrets"
    
    return s1