#!/bin/python3

T = int(input().strip())

stack = []
for _ in range(T):
    in_list = list(input().strip().split(" "))
    inst = in_list[0]

    if inst == 'push':
        stack.append(in_list[1])
    if inst == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    if inst == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if inst == 'size':
        print(len(stack))
    if inst == 'pop':
        if len(stack) != 0:
            print(stack.pop(-1))
        else:
            print(-1)
