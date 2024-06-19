m, seed, x1, x2 = map(int,input().split())
indicator = False
for a in range(m):
    for c in range(m):
        if x1 == ((seed*a +c)% m) and x2 == ((a*x1 +c)% m):
            print(a, c)
            indicator = True
            break
    if indicator:
        break