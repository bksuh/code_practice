def solution(strArr):
    answer = [len(c) for c in strArr]

    idx = set(answer)
    real = [answer.count(id) for id in idx]
    return max(real)