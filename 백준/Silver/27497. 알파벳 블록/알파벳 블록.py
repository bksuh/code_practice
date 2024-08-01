import collections
import sys
input = sys.stdin.readline

queue = collections.deque()
t = int(input())
state = []
for _ in range(t):
    a = tuple(input().rstrip().split())
    if int(a[0]) == 1:
        queue.append(a[1])
        state.append('back')
    elif int(a[0]) == 2:
        queue.appendleft(a[1])
        state.append('front')
    else:
        if queue:
            value = state.pop()
            if value == 'back':
                queue.pop()
            else:
                queue.popleft()

if len(queue) == 0:
    print(0)
else:
    print(''.join(queue))        
        
