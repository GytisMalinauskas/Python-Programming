"""A module for filling spiral matrix of given size with natural numbers"""

def spiral_matrix_f(size):
    top = 0
    bottom = size - 1
    right = size - 1
    left = 0
    matrix = [[0] * size for _ in range(size)]
    row_index = 0
    col_index = 0
    value_index = 1
    
    while bottom >= top and right >= left and value_index <= size**2:
        while col_index <= right:
            ...
        top += 1
        return matrix
    
    return matrix