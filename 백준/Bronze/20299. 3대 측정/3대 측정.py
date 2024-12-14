import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())

teams = []
cnt = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a >= l and b >= l and c >= l and a+b+c >=k:
        teams += [a, b, c]
        cnt +=1
    else:
        continue
print(cnt)
print(*teams)