def solution(arr):
    answer = arr
    idx = 0
    for i in range(len(arr)):
        if pow(2, i) >= len(arr):
            idx = i
            break

    for _ in range(pow(2, idx)-len(arr)):
        answer.append(0)

    return answer