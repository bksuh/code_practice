n = int(input())
for _ in range((n)):
    a = input()
    t = int(pow(len(a), 1/2))
    tmp = []
    for i in range(t):
        tmp.append(a[i*t:t*(i+1)])
    for j in range(t-1, -1, -1):
        for i in range(t):
            print(tmp[i][j], end='')
    print()