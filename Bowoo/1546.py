def new_sc(score):
    return (score/max_num)*100



n = int(input())

sc_list = []

sc_list = input().split()
sc_list = list(map(int, sc_list))

max_num = max(sc_list)

new_sc_list = list(map(new_sc,sc_list))

total = 0
for score in new_sc_list:
    total += score
total /= n
print("%.2f" % total)
