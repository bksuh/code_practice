import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    if a==b:
        print("Possible")
    else:
        print('Impossible')