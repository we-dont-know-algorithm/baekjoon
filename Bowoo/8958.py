import sys

n = int(sys.stdin.readline())

for i in range(n):
    score = 0
    result = 0
    _list = sys.stdin.readline().rstrip()
    for i in _list:
        if i == "X":
            score = 0
        else:
            score += 1
            result += score
    print(result)
