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
        decrypted_state = decrypt_block(block, round_keys)
        plain_block = add_round_key(decrypted_state, prev_block)
        decrypted_blocks.append(plain_block)
        prev_block = block
    return blocks_to_string(decrypted_blocks)
        
def decrypt_pcbc(cipher_blocks, round_keys, iv_block):
    feedback = iv_block
    decrypted_blocks = []
    for block in cipher_blocks:
        decrypted_state = decrypt_block(block, round_keys)
        plain_block = add_round_key(decrypted_state, feedback)
        decrypted_blocks.append(plain_block)
        feedback = add_round_key(block, plain_block)
    return blocks_to_string(decrypted_blocks)

def decrypt_cfb(cipher_blocks, round_keys, iv_block):
    prev_block = iv_block
    decrypted_blocks = []
    for block in cipher_blocks:
        encrypted_prev = encrypt_block(prev_block, round_keys)
        plain_block = add_round_key(encrypted_prev, block)
        decrypted_blocks.append(plain_block)
        prev_block = block
    return blocks_to_string(decrypted_blocks)

def decrypt_ofb(cipher_blocks, round_keys, iv_block):
    keystream_block = iv_block
    decrypted_blocks = []
    for block in cipher_blocks:
        keystream_block = encrypt_block(keystream_block, round_keys)
        plain_block = add_round_key(block, keystream_block)
        decrypted_blocks.append(plain_block)
    return blocks_to_string(decrypted_blocks)