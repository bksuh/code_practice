a, b, c, d = map(int, input().split())

tmp = [list(c for c in input()) for _ in range(a)]
for i in range(len(tmp)):
    for _ in range(c):
        for j in range(len(tmp[i])):
            print(tmp[i][j]*d, end='')
        print()
