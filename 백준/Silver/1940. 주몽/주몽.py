n = int(input())
t = int(input())

arr = list(map(int, input().split()))
cnt =0
for i in range(len(arr)):
    if t-arr[i] in arr:
        cnt +=1

print(cnt//2)