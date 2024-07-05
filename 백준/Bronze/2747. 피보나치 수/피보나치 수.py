n = int(input())
arr=[0,1]
for _ in range(n-1):
    arr.append(arr[-1]+arr[-2])
print(arr[-1])