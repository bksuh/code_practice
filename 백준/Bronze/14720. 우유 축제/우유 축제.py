from collections import deque
t = int(input())
milks = list(map(int, input().split()))
ans = 0
indi = True
seq = deque([1, 2, 0])
for i in range(len(milks)):
    if milks[i] == 0 and indi:
        ans += 1
        indi = False
    if not indi and milks[i] == seq[0]:
        ans +=1
        seq.append(seq.popleft())

print(ans)