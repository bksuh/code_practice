n, m = map(int, input().split())
d = {}
for _ in range(n):
    site, id = input().split()
    d[site] = id

for _ in range(m):
    t = input()
    print(d[t])