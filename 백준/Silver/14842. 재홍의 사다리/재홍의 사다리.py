w, h, n = map(int, input().split())

if n%2 == 0:
    result = (n-2)/4
else:
    result = (n-1)*(n-1) / (4*n)
result *= 2*h
print(result)