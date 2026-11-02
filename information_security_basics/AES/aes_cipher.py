from aes_helpers import sbox, sboxInv, mult_2, mult_3, mult_9, mult_b, mult_d, mult_e

def add_round_key(state, key_block):
    new_state = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            new_state[r][c] = state[r][c] ^ key_block[r][c]
    return new_state

def sub_bytes(state):
    return [[sbox[b] for b in row] for row in state]

def inv_sub_bytes(state):
    return [[sboxInv[b] for b in row] for row in state]

# 3. ShiftRows ir InvShiftRows: poslinkiai eilutėse
def shift_rows(state):
    # Eilutės slenkamos į kairę: 0 per 0, 1 per 1, 2 per 2, 3 per 3
    return [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3]
    ]

def inv_shift_rows(state):
    # Eilutės slenkamos į dešinę: 0 per 0, 1 per 1, 2 per 2, 3 per 3
    return [
        state[0],
        state[1][-1:] + state[1][:-1],
        state[2][-2:] + state[2][:-2],
        state[3][-3:] + state[3][:-3]
    ]

# 4. MixColumns ir InvMixColumns: matricų daugyba stulpeliams
def mix_columns(state):
    new_state = [[0] * 4 for _ in range(4)]
    for c in range(4):
        a0, a1, a2, a3 = state[0][c], state[1][c], state[2][c], state[3][c]
        new_state[0][c] = mult_2[a0] ^ mult_3[a1] ^ a2 ^ a3
        new_state[1][c] = a0 ^ mult_2[a1] ^ mult_3[a2] ^ a3
        new_state[2][c] = a0 ^ a1 ^ mult_2[a2] ^ mult_3[a3]
        new_state[3][c] = mult_3[a0] ^ a1 ^ a2 ^ mult_2[a3]
    return new_state

def inv_mix_columns(state):
    new_state = [[0] * 4 for _ in range(4)]
    for c in range(4):
        a0, a1, a2, a3 = state[0][c], state[1][c], state[2][c], state[3][c]
        new_state[0][c] = mult_e[a0] ^ mult_b[a1] ^ mult_d[a2] ^ mult_9[a3]
        new_state[1][c] = mult_9[a0] ^ mult_e[a1] ^ mult_b[a2] ^ mult_d[a3]
        new_state[2][c] = mult_d[a0] ^ mult_9[a1] ^ mult_e[a2] ^ mult_b[a3]
        new_state[3][c] = mult_b[a0] ^ mult_d[a1] ^ mult_9[a2] ^ mult_e[a3]
    return new_state