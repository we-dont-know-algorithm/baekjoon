#!/bin/python3
import math


def isPrime(n):
    if n <= 1:
        return False
    for q in range(round(math.sqrt(n))+1):
        if q == 0 or q == 1:
            pass
        elif n % q == 0:
            return False
    return True


if __name__ == "__main__":
    nums = list(map(int,input().strip().split(" ")))
    M = nums[0]
    N = nums[1]
    prime_list = []

    for n in range(M,N+1):
        if isPrime(n):
            prime_list.append(n)

    for el in prime_list:
        print(el)
