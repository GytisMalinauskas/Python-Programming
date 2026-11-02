from constants import G, P, A, B
from diffie_hellman import secret_generation

def main():
    print("1. Sugeneruota paslaptis:", secret_generation(G,P,A,B))
    
    
if __name__ == "__main__":
    main()