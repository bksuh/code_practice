import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(input().rstrip().split())
    tmp = float(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == '@':
            tmp *=3
        elif arr[i] =='%':
            tmp +=5
        elif arr[i] =='#':
            tmp -= 7
    print("%.2f" %tmp)