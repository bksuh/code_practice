t = int(input())
s = input()
low, high = [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]
c = 'roygbiv'

for ch in s:
    if ch.lower() in c:
        if ch.isupper():
            high[c.index(ch.lower())]  = 0
        else:
            low[c.index(ch)] = 0

if low == [0, 0, 0, 0, 0, 0, 0] and high == [0, 0, 0, 0, 0, 0, 0]:
    print("YeS")
elif low == [0, 0, 0, 0, 0, 0, 0]:
    print('yes')
elif high == [0, 0, 0, 0, 0, 0, 0]:
    print('YES')
else:
    print("NO!")