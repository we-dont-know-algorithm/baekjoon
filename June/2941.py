#!/bin/python3

word = input().strip()

cnt = 0

alphabets = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for alpha in alphabets:
    if alpha in word:
        cnt += word.count(alpha)
        word = word.replace(alpha," ")

cnt += len(word.replace(" ",""))

print(cnt)
