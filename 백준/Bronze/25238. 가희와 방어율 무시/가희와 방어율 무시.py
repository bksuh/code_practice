a, b = map(int, input().split())
ans = a * (100-b)/100
if ans >= 100:
    print(0)
else:
    print(1)