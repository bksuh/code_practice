n = int(input())
for _ in range(n):
    r, e, c = map(int,input().split())
    tmp = e-c
    if r < tmp:
        print("advertise")
    elif r == tmp:
        print("does not matter")
    else:
        print("do not advertise")