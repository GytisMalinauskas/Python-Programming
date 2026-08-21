ERROR_MESSAGE = "value not in array"

def find(search_list, value):
    search_list = search_list.sort()
    if value < search_list[0] or value > search_list[search_list.count() - 1]:
        raise ValueError(ERROR_MESSAGE)
    