#!/bin/python3
N = int(input().strip())
for i in range(N,0,-1):
    str = " " * (N-i)
    str += "*" * i
    print(str)
