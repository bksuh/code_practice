import collections
import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    target = input().rstrip()
    left = collections.deque()
    right = collections.deque()
    for i in range(len(target)):
        if target[i] =='<':
            if not left:
                continue
            right.appendleft(left.pop())
        elif target[i] =='>':
            if not right:
                continue
            left.append(right.popleft())
        elif target[i] == '-':
            if not left:
                continue
            left.pop()
        else:
            left.append(target[i])
    tmp = list(left+right)
    for elem in tmp:
        print(elem , end='')
    print()