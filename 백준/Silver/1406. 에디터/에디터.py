import collections
import sys

input = sys.stdin.readline
left = collections.deque(input().rstrip())
right = collections.deque()
n = int(input())

for _ in range(n):
    command = tuple(input().rstrip().split())
    if command[0] == 'L':
        if not left:
            continue
        right.appendleft(left.pop())
    elif command[0] == 'D':
        if not right:
            continue
        left.append(right.popleft())
    elif command[0] == 'B':
        if not left:
            continue
        left.pop()
    else:
        left.append(command[1])
ans = list(left + right)
for elem in ans:
    print(elem, end='')