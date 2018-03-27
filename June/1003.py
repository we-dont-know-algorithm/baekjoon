#!/bin/python3

zeros  = [1,0,1]
ones = [0,1,1]
def fib_call(n):
    if n >= 3 :
        length = len(zeros)
        for i in range(length,n+1):
            zeros.append(zeros[i-1]+zeros[i-2])
            ones.append(ones[i-1]+ones[i-2])
    print(str(zeros[n])  + " " + str(ones[n]))


T = int(input().strip())

for i in range(T):
    n = int(input().strip())
    fib_call(n)
