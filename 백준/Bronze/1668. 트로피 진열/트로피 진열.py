n = int(input())

arr = [int(input()) for _ in range(n)]

ans1, ans2 = 1, 1
s = arr[0]

for i in range(1, len(arr)):
    if arr[i] > s:
        s = arr[i]
        ans1 += 1

arr1 = arr[::-1]
s1 = arr1[0]

for i in range(1, len(arr)):
    if arr1[i] > s1:
        s1 = arr1[i]
        ans2 += 1

print(ans1)
print(ans2)