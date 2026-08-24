"""A module to flatten the array"""

def flatten(iterable):
    """Flattens the given list into one"""
    flattened_list=[]
    for value in iterable:
        if isinstance(value, int):
            flattened_list.append(value)
        elif value is None:
            continue
        elif isinstance(value, list):
            for flattened_list_value in flatten(value):
                flattened_list.append(flattened_list_value)
    return flattened_list
