import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(input().rstrip().split())
    for i in range(len(arr)):
        tmp = list(arr[i])
        for c in reversed(tmp):
            print(c, end ='')
        print(' ', end ='')
    print()