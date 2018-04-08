#!/bin/python3

T = int(input().strip())

for i in range(T):
    arr = list(input().strip().split(" "))
    R = int(arr[0])
    _str = arr[1]
    new_str = ''.join(list(map(lambda x: x*R,_str)))
    print(new_str)
