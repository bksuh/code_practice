def solution(x, n):
    answer = []
    t = x
    for _ in range(n):
        answer.append(t)
        t += x
    return answer