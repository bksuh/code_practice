n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

x = list(a.difference(b))
y = list(b.difference(a))

print(len(x)+len(y))