from aes_helpers import (
    byte_string_to_blocks,
    string_to_blocks,
    blocks_to_string,
    blocks_to_byte_string,
    add_round_key,
    inv_shift_rows,
    inv_sub_bytes,
    inv_mix_columns,
    shift_rows,
    sub_bytes,
    mix_columns,
)

def aes_decrypt(text, key):
    cipher_blocks = byte_string_to_blocks(text)
    round_keys = byte_string_to_blocks(key)

    decrypted_blocks = []
    for state in cipher_blocks:
        # Pre-round
        state = add_round_key(state, round_keys[3])

        # 1 raundas
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[2])
        state = inv_mix_columns(state)

        # 2 raundas
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[1])
        state = inv_mix_columns(state)

        # 3 raundas (be InvMixColumns)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[0])

        decrypted_blocks.append(state)

    return blocks_to_string(decrypted_blocks)

def aes_encrypt(plain_text, key_hex):
    blocks = string_to_blocks(plain_text)
    round_keys = byte_string_to_blocks(key_hex)

    encrypted_blocks = []
    for state in blocks:
        # Pre-round
        state = add_round_key(state, round_keys[0])

        # 1 raundas
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[1])

        # 2 raundas
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[2])

        # 3 raundas (be MixColumns)
        state = sub_bytes(state)
        state = shift_rows(state)
        state = add_round_key(state, round_keys[3])

        encrypted_blocks.append(state)

    return blocks_to_byte_string(encrypted_blocks)