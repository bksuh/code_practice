n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1-x2)**2 + (y1-y2)**2
    e = (r1+r2)**2
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif d == e:
        print(1)
    elif d > e:
        print(0)

    elif d == (max(r1, r2) - min(r1, r2))**2:
        print(1)
    elif 0< d < (max(r1, r2) - min(r1, r2))**2:
        print(0)
    else:
        print(2)