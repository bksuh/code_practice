while True:
    a, b, c, d = map(int, input().split())
    if a==0 and b==0 and c==0 and d==0:
        break
    max1 = max(c, d) - min(a, b)
    min1 = min(c, d) - max(a, b)
    print(min1, max1)