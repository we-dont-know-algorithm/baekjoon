#!/bin/python3

nums = list(map(int,input().strip().split(" ")))

N, X = nums[0], nums[1]

arr = list(map(int,input().strip().split(" ")))

new_arr = []
for i in arr:
    if i < X:
        new_arr.append(i)

print(" ".join(map(str,new_arr)))
