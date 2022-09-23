#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 0:
        print("{} arguments.".format(len(argv)))
    elif len(argv) == 1:
        print("{} argument:".format(len(argv)))
        print("{}: {}".format(len(argv), argv[len(argv)]))
    else:
        print("{} argument:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
