n = int(input())

for _ in range(n):
    t = int(input())
    d = {}
    for _ in range(t):
        v = int(input())
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    ans = []
    for k,v in d.items():
        ans.append((k,v))
    ans.sort(key=lambda x : (-x[1], x[0]))
    print(ans[0][0])