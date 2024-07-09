n = int(input())

for _ in range(n):
    a, b, c, d, x, y, z, w = map(int, input().split())
    a = a+x
    b = b+y
    c = c+z
    d = d+w

    if a < 1:
        a = 1
    if b < 1: b=1
    if c < 0: c=0
    ans = a + 5*b + 2*c + 2*d
    print(ans)