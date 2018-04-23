import sys

n = int(sys.stdin.readline())

for i in range(n):
    _list = list(sys.stdin.readline().split())
    repeat = int(_list[0])
    _str = _list[1]
    for letter in _str:
        print(letter * repeat, end="")
    print("")
