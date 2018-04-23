#!/bin/python3

def isGroupword(word):
    pre = word[0]
    _dict = {pre:1}
    for el in word[1:]:
        if el != pre and el in _dict.keys():
            return False
        if el not in _dict.keys():
            _dict[el] = 1

        if el in _dict.keys():
            _dict[el] += 1
        pre = el
    return True

if __name__ == "__main__":
    T = int(input().strip())
    cnt = 0
    for i in range(T):
        word = input().strip()
        if isGroupword(word):
            cnt += 1
    print(cnt)
