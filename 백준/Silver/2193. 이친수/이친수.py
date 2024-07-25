a, b = 1, 0
n = int(input())

for _ in range(1, n):
    tmp = a+b
    a = b
    b = tmp
print(a+b)