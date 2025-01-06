def solution(s1, s2):
    answer = 0
    for elem in s1:
        if elem in s2:
            answer += 1
    return answer