#!/bin/python3

score = int(input().strip())


if score >= 90 and score <= 100:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")
