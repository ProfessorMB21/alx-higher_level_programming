#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number"""
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return (digit)
