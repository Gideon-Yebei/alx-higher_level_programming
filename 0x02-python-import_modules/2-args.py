#!/usr/bin/python3
# 2-args.py
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc - 1))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))

