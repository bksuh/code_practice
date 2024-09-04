n = int(input())
d = {}
for _ in range(n):
    a, b = input().split()
    d[b] = a

tar = input()
ans = ''
for c in tar:
    ans += d[c]
x, y = map(int, input().split())
print(ans[x-1:y])