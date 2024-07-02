n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.reverse()
    length = arr.pop()
    target = sum(arr)/length
    cnt = 0
    for score in arr:
        if target < score:
            cnt+=1
    ans = 100*cnt/length
    
    print(f"{round(ans, 3)}%")