import sys

_str = sys.stdin.readline().rstrip()
abc_str = 'abcdefghijklmnopqrstuvwxyz'

for letter in abc_str:
    if letter in _str:
        print(_str.find(letter), end=" ")
    else:
        print('-1', end=" ")
print("")
