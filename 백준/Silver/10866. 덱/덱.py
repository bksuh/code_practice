import sys
import collections

input = sys.stdin.readline
dq = collections.deque()

n = int(input())
for _ in range(n):
    a = input().rstrip().split()
    if a[0] =='push_front':
        dq.appendleft(a[1])
    elif a[0] =='push_back':
        dq.append(a[1])
    elif a[0] =='pop_front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif a[0] =='pop_back':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    elif a[0] =='size':
        print(len(dq))
    elif a[0] =='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])