_in = input().strip()

total = 0
for s in _in:
    val = ord(s)
    if val in range(ord('A'),ord('C')+1):
        total += 3
    if val in range(ord('D'),ord('F')+1):
        total += 4
    if val in range(ord('G'),ord('I')+1):
        total += 5
    if val in range(ord('J'),ord('L')+1):
        total += 6
    if val in range(ord('M'),ord('O')+1):
        total += 7
    if val in range(ord('P'),ord('S')+1):
        total += 8
    if val in range(ord('T'),ord('V')+1):
        total += 9
    if val in range(ord('W'),ord('Z')+1):
        total += 10
    
print(total)
