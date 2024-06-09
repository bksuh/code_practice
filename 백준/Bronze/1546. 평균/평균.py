n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
for i, score in enumerate(arr):
    arr[i]= (score/m)*100

print(sum(arr)/len(arr))