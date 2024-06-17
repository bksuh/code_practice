a = list(int(c) for c in input())
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i], end='')