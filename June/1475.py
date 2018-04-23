#!/bin/python3

N = input().strip()

_dict = {}
for i in range(9):
    _dict[i] = 0

for s in N:
    if int(s) in _dict.keys():
        _dict[int(s)] += 1
    if int(s) == 9:
        _dict[6] += 1

if _dict[6] % 2 == 0:
    _dict[6] //= 2
else:
    _dict[6] = _dict[6] // 2 + 1

print(max(_dict.values()))
