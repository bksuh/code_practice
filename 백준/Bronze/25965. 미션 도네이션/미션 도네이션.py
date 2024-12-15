t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    for _ in range(n):
        ki, di, ai = map(int, input().split())
        result.append((ki, di, ai))
    x, y, z = map(int, input().split())
    ans = 0
    for i in range(len(result)):
        k, d, a= result[i]
        tmp = x * k + z*a -y*d
        if tmp > 0:
            ans += tmp
    print(ans)