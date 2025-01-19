head = 0

for _ in range(10):
    t = int(input())
    if t == 1:
        head += 90
    elif t == 2:
        head += 180
    else:
        head -= 90
head %= 360

if head == 0:
    print('N')
elif head == 90:
    print('E')
elif head == 180:
    print('S')
else:
    print("W")