#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for element in my_list:
        if element == search:
            idx = my_list.index(element)
            my_list[idx] = replace
    return my_list
