def solution(n):
    answer = ''
    while n//3:
        answer += str(n%3)
        n = n//3
    answer = int(answer+str(n), 3)
    return answer