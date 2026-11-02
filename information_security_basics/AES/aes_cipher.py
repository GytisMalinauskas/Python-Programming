from aes_helpers import byte_string_to_blocks, blocks_to_string, add_round_key, inv_shift_rows, inv_sub_bytes, inv_mix_columns

def aes_decrypt(text, key):
    cipher_blocks = byte_string_to_blocks(text)
    round_keys = byte_string_to_blocks(key)

    state = cipher_blocks[0]

    # --- PRADINIS ŽINGSNIS (Pre-round) ---
    state = add_round_key(state, round_keys[3])

    # --- 1 RAUNDAS ---
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[2])
    state = inv_mix_columns(state)

    # --- 2 RAUNDAS ---
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[1])
    state = inv_mix_columns(state)
    
    # --- 3 RAUNDAS ---
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0])
    
    return blocks_to_string(state)