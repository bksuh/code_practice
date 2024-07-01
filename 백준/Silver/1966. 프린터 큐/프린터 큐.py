import collections

n = int(input())
for _ in range(n):
    x, target = map(int, input().split())
    arr = list(map(int, input().split()))
    dq = collections.deque((i,p) for i, p in enumerate(arr))
    cnt = 0

    while True:
        if dq[0][1] == max(dq,key=lambda x : x[1])[1]:
            cnt+=1
            if dq[0][0] == target:
                break
            dq.popleft()
        else:
            dq.append(dq.popleft())
    print(cnt)