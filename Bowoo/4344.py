import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = sys.stdin.readline().split()
    sum = 0
    for i in range(1,int(n[0])+1):
        sum += int(n[i])
    sum /= int(n[0])
    
    count = 0
    for i in range(1,int(n[0])+1):
        if int(n[i]) > sum:
            count += 1
        else:
            continue
    print('%.3f' % (count/int(n[0])*100) +"%")

