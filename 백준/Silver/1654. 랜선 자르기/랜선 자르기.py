n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]
start = 1
end = max(lines)
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for line in lines:
        cnt += line//mid    
    if cnt < k :
        end = mid-1
    else:
        start = mid + 1
print(end)