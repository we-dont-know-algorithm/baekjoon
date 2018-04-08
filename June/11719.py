#!/bin/python3


while True:
    try:
        line = input()
    except EOFError as e:
        break
    else:
        print(line)
