import sys
import collections

input = sys.stdin.readline
n, k = map(int, input().split())
dq = collections.deque(list(i for i in range(1,n+1)))
ans = []
while True:
    if len(dq) == 0:
        break
    for _ in range(k-1):
        dq.append(dq.popleft())
    ans.append(dq.popleft())

ans1 = list(str(ans))
ans1[0], ans1[-1] ='<', '>'
for element in ans1:
    print(element, end ='')