import math
a, b, c = map(int, input().split())

a = math.ceil(a/c)
b = math.ceil(b/c)

print(int(a*b))