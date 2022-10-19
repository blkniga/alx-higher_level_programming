#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for i in range(list_length):
        result = 0
        try:
            a, b = (my_list_1[i], my_list_2[i])
            result = a / b
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            lst.append(result)
    return lst
