#!/bin/python3

arr = list(input().strip().split(" "))
A,B = arr[0], arr[1]

_reA = int(''.join(reversed(A)))
_reB = int(''.join(reversed(B)))

print(max(_reA,_reB))
