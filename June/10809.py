#!/bin/python3

_str = input().strip()

_dict = {}

for asnum in range(ord('a'), ord('z') + 1):
    _dict[chr(asnum)] = -1

for idx,s in enumerate(_str):
    if _dict[s] == -1:
        _dict[s] = idx


print(' '.join(map(str,list(_dict.values()))))
