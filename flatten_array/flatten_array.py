"""A module to flatten the array"""

def flatten(iterable):
    """Flattens the given list into one"""
    flattened_list=[]
    for value in iterable:
        if value is int:
            flattened_list.append(value)
        if value is None:
            continue
        if value is list:
            flattened_list.append(flatten(value))
    return flattened_list
