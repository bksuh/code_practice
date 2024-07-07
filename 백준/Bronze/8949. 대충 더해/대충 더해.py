a , b = input().split()
a = list(int(c) for c in a)
b = list(int(c) for c in b)

a.reverse()
b.reverse()

arr = []
for i in range(max(len(a), len(b))):
    if i < min(len(a), len(b)):
        arr.append(a[i]+b[i])
    else:
        try: arr.append(a[i])
        except: arr.append(b[i])

arr.reverse()
print(*arr, sep='')