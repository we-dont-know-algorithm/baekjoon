#!/bin/python3


N = int(input().strip())

num = N
cnt = 0
while True:
    _right = num % 10
    _left = num // 10
    _new_right = (_right + _left) % 10
    num = _right * 10 + _new_right
    cnt +=1
    if num == N:
        break
