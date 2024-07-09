n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    cnt = 0
    for _ in range(a):
        x, y, z = map(int, input().split())
        if x*(y/z) >= b:
            cnt+=1
    print(cnt)
    