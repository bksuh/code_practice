subs = []
indi = []
for _ in range(7):
    a, b = input().split()
    b = int(b)
    subs.append(a)
    indi.append(b)

print(subs[indi.index(max(indi))])