n = int(input())

for i in range(n):
    print(f"Data Set {i+1}:")
    ans = 0
    t, s, d = map(int, input().split())
    for _ in range(t):
        di, vi = map(int, input().split())
        if di <= s * d:
            ans += vi
    print(ans)
    print()