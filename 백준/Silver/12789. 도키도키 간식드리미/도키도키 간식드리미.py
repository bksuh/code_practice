from collections import deque
n = int(input())
line = deque(map(int, input().split()))
wait = [0]
ans = []
idx = 1
while line:
    if line[0] == idx:
        ans.append(line.popleft())
        idx += 1
    elif wait[-1] == idx:
        ans.append(wait.pop())
        idx +=1
    else:
        wait.append(line.popleft())
ans = ans + wait[::-1]
ans.pop()
if ans == list(i for i in range(1, n+1)):
    print("Nice")
else:
    print("Sad")