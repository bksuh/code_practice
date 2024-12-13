t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if v * (f /c) >= m:
            cnt += 1
    print(cnt)