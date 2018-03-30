#!/bin/python3
N = int(input().strip())
for i in range(1,N+1):
    str = " " * (N-i)
    str += "*" * i
    print(str)
