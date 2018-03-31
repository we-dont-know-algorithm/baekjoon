#!/bin/python3
sn = [i for i in range(10000)]


for num in range(10000):
    res = num
    for n in str(num):
        res += int(n)
    if res in sn:
        sn.remove(res)


for item in sn:
    print(item)
