#!/bin/python3

def sol():
    word = input().strip().lower()

    _dict = {}

    for ch in range(ord('a'),ord('z')+1):
        _dict[chr(ch)] = 0

    for s in word:
        if s in _dict.keys():
            _dict[s] += 1
        else:
            _dict[s] = 1

    max_val = max(list(_dict.values()))
    m_key = ""
    cnt = 0
    for key,val in _dict.items():
        if val == max_val:
            cnt += 1
            m_key = key

    if cnt > 1:
        print("?")
    else:
        print(m_key.upper())
    return

if __name__ == "__main__":
    sol()
