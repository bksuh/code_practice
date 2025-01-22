a = [c for c in input()]
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a[x], a[y] = a[y], a[x]

s = ''.join(a)
print(s)