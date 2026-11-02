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
    cipher_blocks2 = byte_string_to_blocks(C2)
    iv_block = byt(IV)
    print("1. AES-ECB atviras tekstas:", decrypt_ecb(cipher_blocks, round_keys))
    print("2. AES-CBC atviras tekstas:", decrypt_cbc(cipher_blocks2, round_keys, iv_block))
    
if __name__ == "__main__":
    main()