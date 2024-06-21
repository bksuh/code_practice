import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    tmp = tuple(map(int, input().split()))
    if tmp[0] == 1:
        x = tmp[1]
        arr.append(x)
    elif tmp[0] == 2:
        if len(arr) != 0:
            print(arr.pop(-1))
        else:
            print(-1)
    elif tmp[0] == 3:
        print(len(arr))
    elif tmp[0] == 4:
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    else:
        if len(arr) != 0:
            print(arr[-1])
        else: print(-1)