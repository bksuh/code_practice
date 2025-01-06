import collections

def solution(numbers, k):
    queue = collections.deque(numbers)
    for _ in range(2*(k-1)):
        queue.append(queue.popleft())

    answer = queue[0]
    return answer