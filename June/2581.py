#!/bin/python3
import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    M = int(input().strip())
    N = int(input().strip())
    arr = []

    for num in range(M,N+1):
        if isPrime(num):
            arr.append(num)

    if len(arr) != 0:
        print(sum(arr))
        print(arr[0])
    else:
        print(-1)
