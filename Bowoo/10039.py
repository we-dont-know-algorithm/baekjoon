sum = 0

for i in range(5):
    score = int(input())
    if score < 40:
        sum += 40
    else:
        sum += score

print(int(sum/5))
