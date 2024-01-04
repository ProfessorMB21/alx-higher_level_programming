#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of 1 + 2"""
    from add_0 import add
    a, b = 1, 2
    total = add(a, b)
    print("{0} + {1} = {2}".format(a, b, total))
