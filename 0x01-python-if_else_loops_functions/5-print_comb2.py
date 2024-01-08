#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0{}".format(i), sep=", ")
    elif i >= 10 and i != 100:
        print("{}".format(i), sep=", ")
