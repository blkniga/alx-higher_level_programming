#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 0:
        print("{} arguments.".format(len(argv)))
    elif len(argv) == 1:
        print("{} argument:".format(len(argv)), "{}: {}".format(1, argv[1]))
    else:
        print("{} arguments.".format(len(argv)))
        for i in range(1, len(arg) + 1):
            print("{}: {}".format(i, argv[i]))
