#!/bin/python3

T = int(input().strip())

for _ in range(T):
    hotel = list(map(int,input().strip().split(" ")))
    H = hotel[0]
    W = hotel[1]
    customer = hotel[2]
    if customer % H != 0:
        room_num = str(customer % H)
        if customer // H < 9:
            room_num += '0'
        room_num += str(customer // H + 1)
    else:
        room_num = str(H)
        if customer // H < 10:
            room_num += '0'
        room_num +=  str(customer // H)

    print(room_num)
