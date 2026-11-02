from aes_cipher import add_round_key, inv_shift_rows, inv_sub_bytes, inv_mix_columns
from aes_helpers import byte_string_to_blocks, blocks_to_string
from constants import KEY, TEXT

def main():
    cipher_blocks = byte_string_to_blocks(TEXT)
    round_keys = byte_string_to_blocks(KEY)

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
    state = add_round_key(state, round_keys[3])
    state = inv_mix_columns(state)
    # --- 3 RAUNDAS ---
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[3])
    state = inv_mix_columns(state)