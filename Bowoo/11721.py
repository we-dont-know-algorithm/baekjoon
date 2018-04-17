import sys

_str = sys.stdin.readline().rstrip()

for i in range(len(_str)):
    print(_str[i], end="")
    if i%10 is 9:
        print("")
    else:
        continue
print("")
