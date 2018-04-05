N = int(input())

N5 = N % 5

if N5 == 0 :
    print(N//5)
elif ((N5 == 1) and (N >= 6)) or (N5 == 3):
    print(N//5+1)
elif ((N5 == 2) and (N >= 12)) or ((N5 ==4) and (N >= 9)):
    print(N//5+2)
else:
    print("-1")
