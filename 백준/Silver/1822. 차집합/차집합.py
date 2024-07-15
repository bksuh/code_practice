n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

x = list(a.difference(b))

print(len(x))
if len(x) != 0:
    x.sort()
    print(*x)