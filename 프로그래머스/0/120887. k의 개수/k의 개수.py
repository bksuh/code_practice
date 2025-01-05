def solution(i, j, k):
    answer = ''
    for x in range(i, j+1):
        answer += str(x)
    return answer.count(str(k))