#!/bin/python3


while True:
    try:
        line = input().strip()
    except EOFError as e:
        break
    else:
        print(line)
