#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1 + a, 10):
        print("{:d}{:d}".format(a, b), end="")
        if (a + b) is not 17:
            print(",", end=" ")
print()
