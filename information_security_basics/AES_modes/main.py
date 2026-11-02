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
from aes_helpers import byte_string_to_blocks

def main():
    round_keys = byte_string_to_blocks(KEY)
    cipher_blocks = byte_string_to_blocks(C1)
    print("1. AES-ECB atviras tekstas:", decrypt_ecb(cipher_blocks, round_keys))
    
if __name__ == "__main__":
    main()