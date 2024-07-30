t = int(input())
res = []
for _ in range(t):
    tmp = input()
    cnt = 0
    for c in tmp:
        if c.isdigit():
            cnt+=int(c)
    res.append((len(tmp), cnt, tmp))
res.sort(key = lambda x : (x[0], x[1], x[2]))
for k in res:
    print(k[2])