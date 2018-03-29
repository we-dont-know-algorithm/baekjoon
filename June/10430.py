#!/bin/python3

arr = list(map(int,(input().strip().split(" "))))
A = arr[0]
B = arr[1]
C = arr[2]

print(str((A+B)%C))
print(str((A%C + B%C)%C))
print(str((A*B)%C))
print(str((A%C * B%C)%C ))
