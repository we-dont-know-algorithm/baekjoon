#!/bin/python3

apart = [[0] * 14 for i in range(14)]
# 14*14 매트릭스 생성

for idx in range(14):
    apart[0][idx] = idx + 1
    apart[idx][0] = 1

def find(a,b):
    if b == 1 :
        return 1
    if apart[a][b-1] != 0:
        return apart[a][b-1]

    apart[a][b-1] = find(a-1,b) + find(a,b-1)
    return apart[a][b-1]

T = int(input().strip())

for _ in range(T):
    a = int(input().strip())
    b = int(input().strip())
    #  a층 b 호, b-1 번째 배열
    print(find(a,b))
