t = int(input())
arr = [0 for _ in range(t+1)]
arr[1], arr[2] = 1, 2
for k in range(3, t + 1):
    arr[k] = arr[k-1]%10 + arr[k-2]%10
print(str(arr[t])[-1])