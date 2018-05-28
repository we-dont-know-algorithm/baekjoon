import sys

_dict={}

_str = sys.stdin.readline().rstrip()
new_str = _str.upper()

for letter in new_str:
    if letter in _dict:
        continue
    else:
        _dict[letter] = new_str.count(letter)

values = list(_dict.values())

if values.count(max(values)) != 1:
    print("?")
else:
    for key in _dict:
        if _dict[key] == max(values):
            print(key)
        else:
            continue
