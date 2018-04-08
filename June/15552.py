#!/bin/python3
import sys

T = int(input().strip())

for i in range(T):
    arr = list(map(int,sys.stdin.readline().split(" ")))
    print(str(arr[0] + arr[1]))
