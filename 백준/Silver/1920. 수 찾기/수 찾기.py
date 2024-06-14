import sys

n = int(sys.stdin.readline())

arrn = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arrm = list(map(int, sys.stdin.readline().split()))
for i in range(len(arrm)):
    if arrm[i] in arrn:
        print(1)
    else:
        print(0)