import sys

try:
    a = sys.stdin.readlines()
except EOFError:
    pass

for line in a:
    print(line, end="")
