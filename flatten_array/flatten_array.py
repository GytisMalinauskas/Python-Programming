"""A module to flatten the array"""

def flatten(iterable):
    """Flattens the given list into one"""
    flattened_list=[]
    for value in iterable:
        if isinstance(value, int):
            flattened_list.append(value)
        elif isinstance(value, None):
            continue
        elif isinstance(value, list):
            for v in flatten(value):
                flattened_list.append(v)
    return flattened_list
