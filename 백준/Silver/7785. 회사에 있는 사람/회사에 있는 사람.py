n = int(input())
d ={}
for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        d[a] = True
    elif b =='leave':
        if a in d:
            del d[a]

ans = list(d.keys())
ans.sort(reverse=True)
print(*ans, sep='\n')