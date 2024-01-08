#!/usr/bin/python3
if __name__ == "__main__":
    """Does some math"""
    import calculator_1

    a = 10
    b = 5
    sum = calculator_1.add(a, b)
    diff = calculator_1.sub(a, b)
    prod = calculator_1.mul(a, b)
    quo = calculator_1.div(a, b)
    print("{0} + {1} = {2}".format(a, b, sum))
    print("{0} - {1} = {2}".format(a, b, diff))
    print("{0} * {1} = {2}".format(a, b, prod))
    print("{0} / {1} = {2}".format(a, b, quo))
