num_list = list(map(int,input().strip().split()))

A = num_list[0]
B = num_list[1]
C = num_list[2]

print( (A+B)%C )
print( (A%C + B%C)%C )

print( (A*B)%C )
print((A%C * B%C)%C)


