#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = []
    for element in my_list:
        lst.append(element)
    for element in lst:
        if element == search:
            idx = lst.index(element)
            lst[idx] = replace
    return lst
