import sys


month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, sys.stdin.readline().split())

total = 0
for i in range(x):
    total += month[i]
total += y

print(day[total%7])

