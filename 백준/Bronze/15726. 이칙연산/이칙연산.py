x, y, z = map(int, input().split())
a = x * y / z
b = x / y * z
print(int(max(a,b)))