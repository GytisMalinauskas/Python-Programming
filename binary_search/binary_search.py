"""A module for binary search algorithm"""
ERROR_MESSAGE = "value not in array"

def find(search_list, value):
    """Finds the value from the list by splitting the list in half"""
    bound
    index = len(search_list) - 1
    rotation_count = 0
    while index > 0:
        if value < search_list[0] or value > search_list[len(search_list) - 1]:
            raise ValueError(ERROR_MESSAGE)
        if index % 2 != 0:
            index = int(index / 2 + 1)
        else:
            index = int(index / 2)
        if search_list[index] == value:
            return rotation_count
        elif search_list[index] > value:
            new_index = len(search_list) - 1
            while new_index >= index:
                search_list.pop(new_index)
                new_index -= 1
            index = new_index
        elif search_list[index] < value:
            new_index = 0
            while new_index <= index:
                search_list.pop(0)
                new_index += 1
            index = len(search_list) - 1
        rotation_count += 1
    return rotation_count