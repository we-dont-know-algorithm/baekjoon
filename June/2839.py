#!/bin/python3

def sol(N):
    ret = N % 5
    if ret == 0:
        return N // 5
    else:
        if ret == 3 :
            return N // 5 + 1
        elif ret == 4 :
            if N // 5 >= 1 :
                return N // 5 - 1 + 3
            else:
                return -1
        elif ret == 1 :
            if N // 5 >= 1 :
                return N // 5 - 1 + 2
            else:
                return -1
        elif ret == 2 :
            if N // 5 >= 2:
                return N // 5 - 2 + 4
            else:
                return -1

if __name__ == "__main__":
    N = int(input().strip())
    print(sol(N))
