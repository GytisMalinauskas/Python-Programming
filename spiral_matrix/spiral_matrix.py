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
            matrix[row_index][col_index] = value_index
            value_index += 1
            if value_index > size**2:
                return matrix
            if col_index < right:
                col_index +=1
        top += 1
        while row_index <= bottom:
            matrix[row_index][col_index] = value_index
            value_index += 1
            if row_index < bottom:
                row_index += 1
        right += 1
        while col_index >= left:
            matrix[row_index][col_index] = value_index
            value_index += 1
            if col_index > left:
                col_index -= 1
        bottom -= 1
        while row_index >= top:
            matrix[row_index][col_index] = value_index
            value_index += 1
            if row_index > top:
                row_index -= 1
        bottom -= 1
        return matrix
    
    return matrix