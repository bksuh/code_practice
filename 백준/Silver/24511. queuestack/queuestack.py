t = int(input())
stack_queue = list(map(int, input().split()))
arr = list(map(int, input().split()))
n = int(input())
next_num = list(map(int, input().split()))
import collections
queue = collections.deque()
for i in range(t):
    if stack_queue[i] == 0:
        queue.append(arr[i])
for elem in next_num:
    queue.appendleft(elem)
    print(queue.pop(), end =' ')