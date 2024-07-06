n = int(input())
for _ in range(n):
    a = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = [max(arr)- min(arr)]
    for i in range(len(arr)-1):
        tmp.append(arr[i+1]-arr[i])
    print(sum(tmp))