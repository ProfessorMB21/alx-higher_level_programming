#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0:
            print("0{}".format(j), end=", ")
        else:
            if i == 8:
                print("{0}{1}".format(i, j), end="\n")
            else:
                print("{0}{1}".format(i, j), end=", ")
