#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for element in my_list[:x]:
            print(element, end='')
    except Exception as error:
        print(f'{error}')
