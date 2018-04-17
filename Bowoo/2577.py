import sys 

result = 1

for i in range(3):
    result *= int(sys.stdin.readline().rstrip())

_str = str(result)

for i in range(10):
    print(_str.count(str(i)))
