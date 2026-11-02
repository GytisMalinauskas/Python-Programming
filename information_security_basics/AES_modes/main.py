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
    iv_block = byte_string_to_blocks(IV)[0]

    cb1 = byte_string_to_blocks(C1)
    cb2 = byte_string_to_blocks(C2)
    cb3 = byte_string_to_blocks(C3)
    cb4 = byte_string_to_blocks(C4)
    cb5 = byte_string_to_blocks(C5)

    print("1. AES-ECB atviras tekstas:", decrypt_ecb(cb1, round_keys))
    print("2. AES-CBC atviras tekstas:", decrypt_cbc(cb2, round_keys, iv_block))
    print("3. AES-PCBC atviras tekstas:", decrypt_pcbc(cb3, round_keys, iv_block))
    print("4. AES-CFB atviras tekstas:", decrypt_cfb(cb4, round_keys, iv_block))
    print("5. AES-OFB atviras tekstas:", decrypt_ofb(cb5, round_keys, iv_block))    

if __name__ == "__main__":
    main()