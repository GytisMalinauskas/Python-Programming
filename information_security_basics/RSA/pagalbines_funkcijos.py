def byte_length(input):
	return (input.bit_length() + 7) // 8

def string_to_bytes(input):
	return str.encode(input)

def bytes_to_int(input):
	return int.from_bytes(input, 'big')

def int_to_bytes(input):
	return input.to_bytes(byte_length(input), 'big')

def bytes_to_string(input):
	return input.decode("utf-8")

def int_to_string(input):
	return bytes_to_string(int_to_bytes(input))

def string_to_int(input):
	return bytes_to_int(string_to_bytes(input))

def integer_root(c: int, e: int) -> int:
    """Returns floor of the e-th root of c using binary search."""
    lo, hi = 0, c
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** e <= c:
            lo = mid
        else:
            hi = mid - 1
    return lo

