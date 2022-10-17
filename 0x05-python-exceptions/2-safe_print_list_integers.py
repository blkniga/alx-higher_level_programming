#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no = 0
    for element in range(x):
        try:
            print('{:d}'.format(my_list[element]), end='')
            no = no + 1
        except IndexError:
            raise
        except Exception:
            continue
    print('')
    return no
