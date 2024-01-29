#!/usr/bin/python3

def safe_print_division(a, b):
    """ Divides 2 integers and prints the result """

    try:
        total = float(a) / b
    except ZeroDivisionError:
        total = None
    finally:
        print("Inside result: {}".format(total))
    return total
