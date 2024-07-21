n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
tip = 0
for i in range(n):
    if arr[i] - i < 0:
        continue
    tip += arr[i] - i
print(tip)
