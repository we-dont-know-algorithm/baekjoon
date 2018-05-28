import sys

_list=[]
n = int(sys.stdin.readline())

for i in range(n):
    _list.append(int(sys.stdin.readline()))

_list_sorted = sorted(_list)

# print arithmetic mean
print(int(sum(_list_sorted)/len(_list_sorted)))

# print median value
print(_list_sorted[len(_list_sorted)//2])

# print mode
mode_list = []
for x in _list_sorted:
    if _list_sorted.count(x) == max(_list.count(x) for x in _list):
        if x not in mode_list:
            mode_list.append(x)

if len(mode_list) != 1:
    mode_list.pop(0)

print(mode_list[0])

# print range of numbers
print(_list_sorted[-1]-_list_sorted[0])
