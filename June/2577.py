#!/bin/python3

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

pair = { str(i) : 0 for i in range(0,10)}

res = A * B * C

for s in str(res):
    if s in pair.keys():
        pair[s] += 1

for key in pair.keys():
    print(pair[key])
