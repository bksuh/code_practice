import collections

n = int(input())
nums = collections.deque(i for i in range(1, n+1))
commands = list(map(int, input().split()))
result = []
ans = [0] * n
for command in commands:
    if command == 1:
        result.append(nums.popleft())
    elif command == 3:
        result.append(nums.pop())
    else:
        tmp = nums.popleft()
        result.append(nums.popleft())
        nums.appendleft(tmp)
for idx in result:
    ans[idx-1] = n
    n-=1
print(*ans)