from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = deque([arr.popleft()])

    for i in range(len(arr)):
        if answer[-1] != arr[0]:
            answer.append(arr.popleft())
        else:
            arr.popleft()
    return list(answer)