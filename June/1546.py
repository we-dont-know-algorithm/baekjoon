#!/bin/python3

N = int(input().strip())

arr = list(map(int, input().strip().split(' ')))

M = 0
sum = 0
for item in arr:
    sum += item
    if item > M:
        M = item
avg = sum / N
new_avg = avg / M * 100
print(round(new_avg,2))
