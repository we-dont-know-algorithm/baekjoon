import sys

_list_count=[0 for x in range(10001)]

n = int(sys.stdin.readline())
for i in range(n):
    _list_count[int(sys.stdin.readline())] += 1

for x in range(10001):
    if _list_count[x] != 0:
        print( (str(x)+" ") * _list_count[x], end="")
    else:
        continue
print("")
