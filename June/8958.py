#!/bin/python3


N = int(input().strip())


for i in range(N):
    quiz = input().strip()
    cntO = 0
    score = 0
    for s in quiz:
        if s == "X":
            score += (cntO ** 2 + cntO) / 2
            cntO = 0
        else:
            cntO += 1
    score += (cntO ** 2 + cntO) / 2
    print(int(score))
