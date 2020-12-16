#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    if x == 1:
        print("0-arguments.")
        exit()
    elif x == 2:
        print("1 argument:\n: {}".format(argv[1]))
    else:
        print("{} arguments:".format(x - 1))
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
