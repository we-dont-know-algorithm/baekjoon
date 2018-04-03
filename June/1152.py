#!/bin/python3

line = input().strip().split(" ")

if line[-1] != "":
    print(len(line))
else:
    print(len(line) - 1)
