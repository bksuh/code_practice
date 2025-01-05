def solution(arr, k):
    answer = []
    for elem in arr:
        if elem not in answer:
            answer.append(elem)
        if len(answer) == k:
            break
    for _ in range(k-len(answer)):
        answer.append(-1)
    return answer