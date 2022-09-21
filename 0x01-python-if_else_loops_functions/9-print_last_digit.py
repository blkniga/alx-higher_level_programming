#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        answer = number % 10
    else:
        answer = number % -10
    return(answer)

