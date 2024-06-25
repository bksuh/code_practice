a, b, c = map(int, input().split())
tmp = a*b

if tmp > c:
    print(tmp-c)
else:
    print(0)