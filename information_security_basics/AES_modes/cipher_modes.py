from aes_cipher import decrypt_block, encrypt_block
from aes_helpers import blocks_to_string, add_round_key

def decrypt_ecb(cipher_blocks, round_keys):
    decrypted_blocks = []
    for block in cipher_blocks:
        decrypted_blocks.append(decrypt_block(block, round_keys))
    return blocks_to_string(decrypted_blocks)
    
def decrypt_cbc(cipher_blocks, round_keys, iv_block):
    prev_block = iv_block
    decrypted_blocks = []
    for block in cipher_blocks:
        decrypted_block = decrypt_block(block, round_keys)
        add_round_key(prev_block, round_keys)
        prev_block = decrypted_block
    return blocks_to_string(decrypted_blocks)
        
def decrypt_pcbc(cipher_blocks, round_keys, iv_block):
    ...
    
def decrypt_cfb(cipher_blocks, round_keys, iv_block):
    ...
    
def decrypt_ofb(cipher_blocks, round_keys, iv_block):
    ...