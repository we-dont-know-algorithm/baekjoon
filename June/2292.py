#!/bin/python3
import math

k = int(input().strip())

result = round(math.sqrt((k-1)/3)) + 1
print(result)

# 1+ sum 6(n-1)
#
# = 1 + 3(n-1)n
# n이 층수이고
#
# k라는 수가 주어졌을 때
# 1+ 3(n-2)(n-1) < k <= 1 + 3(n-1)n
# 인 n을 구하는 것이 문제 해결
#
# (n-2)(n-1) < (k-1)/3 <= (n-1)n
# (n-1)(n-2)+1 <= (k-1)/3 <= n(n-1)
#
# (n-1)(n-2)+1 > (n-3/2)^2
# (n-1)(n)  < (n-1/2)^2
#
# (n-3/2) <= {(k-1)/3}^(1/2) < (n-1/2)
# 
# So, we have that rounded middle term comes n-1
#
# 그래서 마지막에 1을 더해주는거임~
