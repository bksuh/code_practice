def solution(rank, attendance):
    answer = []
    for i,v in enumerate(attendance):
        if v:
            answer.append((i, rank[i]))
    answer.sort(key = lambda x: x[1])
    real = 10000*answer[0][0]+100*answer[1][0] + answer[2][0]
    return real