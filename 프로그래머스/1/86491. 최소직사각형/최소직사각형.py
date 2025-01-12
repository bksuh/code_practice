def solution(sizes):
    n, m = 0, 0
    for h, w in sizes:
        n = max(max(h, w), n)
        m = max(min(h,w), m)
    answer = n*m
    return answer