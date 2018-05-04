import sys

_str = sys.stdin.readline().rstrip()
_list=[]

for letter in _str:
    _list.append(int(letter))

_list_sorted = sorted(_list, reverse=True)

for x in _list_sorted:
    print(x, end="")
print("")
