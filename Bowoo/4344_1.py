import sys

t = int(sys.stdin.readline())

for i in range(t):
    n_list = sys.stdin.readline().rstrip().split()
    n = int(n_list.pop(0))
    n_list  = list(map(int, n_list))
   
    sum = 0
    for x in n_list:
        sum += x
    sum /= n

    count = 0
    for x in n_list:
        # print(x)
        if x > sum:
            count += 1
        else:
            continue

    print('%.3f' % (count/n*100) +"%")

