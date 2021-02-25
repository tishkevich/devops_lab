#!/usr/bin/env python

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
output = {}
for i in range(len(list1)):
    output[list1[i]] = list2[i] if len(list2) > i else None
print(output)
