n = int(input())
arr = [c for c in range(n+1)]
for k in range(3, n+1):
    arr[k] = arr[k-1] + arr[k-2]
print(arr[n]%10007)