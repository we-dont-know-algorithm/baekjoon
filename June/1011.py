#!/bin/python3
import math
T = int(input().strip())

for _ in range(T):
    _in = list(map(int,input().strip().split(" ")))
    x,y = _in[0], _in[1]
    dist = y-x
    n = math.floor(math.sqrt(dist))
    cnt = n*2 - 1
    if dist > n**2 :
        cnt +=1
    if dist > n**2 + n :
        cnt +=1
    print(cnt)
