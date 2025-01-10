n = int(input())
arr = [0 for _ in range(n+1)]
arr[1] = 1
if n>=2:
    arr[2] = 3
for i in range(3, n+1):
    arr[i] = arr[i-1] + 2*arr[i-2]
print(arr[-1] % 10007)