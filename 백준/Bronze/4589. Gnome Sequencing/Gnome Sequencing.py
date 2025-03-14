n = int(input())
print("Gnomes:")
for _ in range(n):
    arr = list(map(int, input().split()))
    tmp = sorted(arr)
    tmp1 = sorted(arr, reverse=True)
    if arr == tmp or arr==tmp1:
        print('Ordered')
    else:
        print("Unordered")