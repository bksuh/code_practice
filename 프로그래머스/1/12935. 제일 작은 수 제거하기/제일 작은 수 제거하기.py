def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        t = min(arr)
        for elem in arr:
            if t == elem:
                continue
            else:
                answer.append(elem)
    return answer