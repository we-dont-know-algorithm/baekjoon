#!/bin/python3

days = [0,31,59,90,120,151,181,212,243,273,304,334]

arr = list(map(int,input().strip().split(" ")))

m = arr[0]
d = arr[1]

days_passed = days[m-1] + d - 1

day = days_passed % 7

if day == 0:
    print("MON")
if day == 1:
    print("TUE")
if day == 2:
    print("WED")
if day == 3:
    print("THU")
if day == 4:
    print("FRI")
if day == 5:
    print("SAT")
if day == 6:
    print("SUN")
