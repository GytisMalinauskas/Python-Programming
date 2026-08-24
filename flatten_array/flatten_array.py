"""A module to flatten the array"""

def flatten(iterable):
    """Flattens the given list into one"""
    flattened_list=[]
    for value in iterable:
        if type(value) is int:
            flattened_list.append(value)
        elif type(value) is None:
            continue
        elif type(value) is list:
            for v in flatten(value):
                flattened_list.append(v)
    return flattened_list
