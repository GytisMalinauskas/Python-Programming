from constants import G, P, A, B, G2, P2, X
from diffie_hellman import secret_generation, baby_step_giant_step, generate_prime

def main():
    print("1. Sugeneruota paslaptis:", secret_generation(G,P,A,B))
    print("2. Rastas a:", baby_step_giant_step(G2, P2, X))
    print("3. Rastas pirminis skaičius: ", generate_prime(bits=100, g=2))
    
if __name__ == "__main__":
    main()