n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key= lambda x: (x[1], x[0]))
end_time = arr[0][1]
ans = 1
for i in range(1, len(arr)):
    if arr[i][0] < end_time:
        continue
    end_time = arr[i][1]
    ans+=1

print(ans)