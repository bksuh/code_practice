n = int(input())
ans = [1,2,3,4,5,1,2,3,4,5]
for i in range(n):
    arr = list(map(int, input().split()))
    if arr == ans:
        print(i+1)