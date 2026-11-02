from cipher_modes import (
    decrypt_cbc,
    decrypt_cfb,
    decrypt_ecb,
    decrypt_ofb,
    decrypt_pcbc
)
from constants import (
    KEY,
    C1,
    C2,
    C3,
    C4,
    C5,
    IV
)

def main():
    print("1. Dešifruotas tekstas:", decrypt_ecb(C1, KEY))
    
if __name__ == "__main__":
    main()