import sys

n, x = map(int, sys.stdin.readline().split())

n_list = sys.stdin.readline().rstrip().split()

for i in n_list:
    if int(i) < x:
        print(i,end=" ")
    else:
        continue
print("")
