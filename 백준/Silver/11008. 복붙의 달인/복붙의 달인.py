n = int(input())

for _ in range(n):
    a, b = input().split()
    tmp = a.count(b)
    ans = tmp + len(a)  - tmp * (len(b))
    print(ans)