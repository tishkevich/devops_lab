#!/usr/bin/env python

path = input()
up = 0
right = 0
for i in range(len(path)):
    if path[i] == "U":
        up += 1
    elif path[i] == "D":
        up -= 1
    elif path[i] == "R":
        right += 1
    elif path[i] == "L":
        right -= 1

print(up == 0 and right == 0)
