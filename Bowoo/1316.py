import sys

n = int(sys.stdin.readline())
count = 0

for i in range(n):
    _word = sys.stdin.readline().rstrip()
    count += 1
    _list=[]

    for letter in _word:
        if letter not in _list:
            _list.append(letter)
        else:
            if letter == _list[-1]:
                continue
            else:
                count -= 1
                break
        
print(count)
