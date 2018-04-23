import sys

_cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

_str = sys.stdin.readline().rstrip()

for item in _cro:
    _str = _str.replace(item, 'R')

print(len(_str))
