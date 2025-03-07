t, x = map(int, input().split())
n = int(input())
cnt = 0
for _ in range(n):
    a = int(input())
    arr = list(map(int, input().split()))
    if x in arr:
        cnt += 1

print('YES' if cnt == n else 'NO')