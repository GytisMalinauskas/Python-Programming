"""A module for binary search algorithm"""
ERROR_MESSAGE = "value not in array"

def find(search_list, value):
    """Finds the value from the list by splitting the list in half"""
    lower_bound = 0
    upper_bound = len(search_list) - 1
    while True:
        if value < search_list[lower_bound] or value > search_list[upper_bound]:
            raise ValueError(ERROR_MESSAGE)
        index = (upper_bound + lower_bound) // 2
        middle_value = search_list[index]
        if middle_value == value:
            return index
        elif middle_value > value:
            upper_bound = index - 1
        elif middle_value < value:
            lower_bound = index + 1
        if lower_bound > upper_bound:
            raise ValueError(ERROR_MESSAGE)