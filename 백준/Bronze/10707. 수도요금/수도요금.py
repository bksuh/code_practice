arr = list(int(input()) for _ in range(5))
a = arr[-1]*arr[0]

b = arr[1]
if arr[4] > arr[2]:
    b += (arr[4]-arr[2])*arr[3]

print(min(a, b))