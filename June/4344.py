#!/bin/python3

C = int(input().strip())

for i in range(C):
    arr = list(map(int,input().strip().split(" ")))
    N = arr[0]
    del arr[0]
    avg = sum(arr) / N
    cnt = 0
    for num in arr:
        if num > avg:
            cnt += 1
    print("%.3f"%(cnt/N*100)+"%")
