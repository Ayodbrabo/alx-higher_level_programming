#!/usr/bin/python3
def uppercase(s):
    """Print a string in uppercase."""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 123:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
