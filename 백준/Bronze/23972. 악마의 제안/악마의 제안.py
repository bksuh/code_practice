k, n = map(int, input().split())

if n == 1 : print(-1)
else:
    T = (n*k)//(n-1)
    if (k*n) % (n-1):
        T += 1
    print(T)