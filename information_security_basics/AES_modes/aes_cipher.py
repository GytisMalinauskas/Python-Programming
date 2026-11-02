from aes_helpers import (
    add_round_key,
    inv_shift_rows,
    inv_sub_bytes,
    inv_mix_columns,
    shift_rows,
    sub_bytes,
    mix_columns,
)

def decrypt_block(state, round_keys):
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

    return state

def encrypt_block(state, round_keys):
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

    return state