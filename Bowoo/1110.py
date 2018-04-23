import sys

n = int(sys.stdin.readline())
n_original = n
cycle = 0
d_10 = 0  # digit for tens
d_1 = 0 # digit for units

while True:
    cycle += 1
    d_10 = n//10
    d_1 = n%10

    n = d_1*10 + (d_10+d_1)%10
    
    if n == n_original:
        break
    
print(cycle)


