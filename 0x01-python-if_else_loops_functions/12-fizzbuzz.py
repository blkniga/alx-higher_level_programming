#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            a = "Fizz"
        elif i % 3 == 0 and i % 5 == 0:
            a = "FizzBuzz"
        else:
            a = i
    print("{}".format(a), end=" ")
