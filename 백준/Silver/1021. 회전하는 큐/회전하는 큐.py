import collections
n, m = map(int, input().split())
picker = collections.deque(i for i in range(1, n+1))
target = list(map(int, input().split()))
cnt = 0
for i in range(len(target)):
    while True:
        if target[i] == picker[0]:
            picker.popleft()
            break
        tmp = picker.index(target[i])
        if tmp > len(picker)-1 - tmp:
            picker.appendleft(picker.pop())
        else:
            picker.append(picker.popleft())
        cnt+=1

print(cnt)