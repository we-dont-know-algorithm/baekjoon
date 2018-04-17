#!/bin/python3


def isPrime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    N = int(input().strip())

    arr = list(map(int,input().strip().split(" ")))
    cnt = 0
    for el in arr:
        if isPrime(el):
            cnt +=1
    print(cnt)
