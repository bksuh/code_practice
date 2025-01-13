n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr1 = list(map(int,input().split()))

ans = sum(arr)

for elem in arr1:
    if elem == 0:
        continue
    ans *= elem

print(ans)