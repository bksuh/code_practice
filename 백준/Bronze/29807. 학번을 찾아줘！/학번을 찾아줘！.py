n = int(input())
arr = list(map(int, input().split()))

while len(arr) != 5:
    arr.append(0)

ans = abs(arr[0]-arr[2])

if arr[0] > arr[2]:
    ans *= 508
else:
    ans *= 108

tmp = abs(arr[1] - arr[3])
if arr[1] > arr[3]:
    tmp *= 212
else:
    tmp *= 305

real = ans + tmp

b = arr[4] * 707
real += b

print(real * 4763)