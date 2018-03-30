#!/bin/python3

word = input().strip()
length = len(word)
q = length // 10
for i in range(0,q):
    print(word[10*i:10*(i+1)])

if length > 10*q:
    print(word[10*q:])
