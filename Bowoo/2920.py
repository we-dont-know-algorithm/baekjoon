import sys

_list = list(map(int, sys.stdin.readline().rstrip().split()))

if _list == sorted(_list):
    print("ascending")
elif _list == sorted(_list, reverse=True):
    print("descending")
else:
    print("mixed")
