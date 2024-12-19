t = int(input())

for _ in range(t):
    N = int(input())
    info = []
    for _ in range(N):
        a, b = map(int, input().split())
        info.append((a, b, b/a))
    info.sort(key=lambda x: (x[2], x[1]))

    print(info[0][1])
