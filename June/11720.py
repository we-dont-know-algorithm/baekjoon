#!/bin/python3

N = int(input().strip())
arr = map(int,input().strip())
sum = 0
for item in arr:
    sum += int(item)
print(str(sum))
