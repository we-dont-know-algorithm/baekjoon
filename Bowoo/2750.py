import sys

_list=[]
n = int(sys.stdin.readline())
for i in range(n):
    _list.append(int(sys.stdin.readline()))

list_sorted = sorted(_list)
for i in list_sorted:
    print(i)
