from math import sqrt
import sympy

def secret_generation(g, p, a, b):
    A = pow(g,a,p)
    B = pow(g,b,p)
    s1 = pow(B,a,p)
    s2 = pow(A,b,p)
    assert s1 == s2, "Wrong secrets"
    
    return s1

def baby_step_giant_step(g, p, x):
    m = int(sqrt(p - 1))
    values = {}
    for j in range(m):
        v = pow(g, m*j, p)
        values[v] = j
    for i in range(m-1):
        v2 = pow(g, -i, p) * x
        if v2 in values.keys():
            break
    
def generate_prime(bits, g):
    ...