#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    result = 0
    ctrl = 0
    for i1, i2 in zip(my_list_1, my_list_2):
        try:
            result = i1 / i2
            lst.append(result)
        except ZeroDivisionError:
            print('division by 0')
            lst.append(ctrl)
        except TypeError:
            print('wrong type')
            lst.append(ctrl)
        except IndexError:
            print('out of range')
            lst.append(ctrl)
        finally:
            pass
    return lst
