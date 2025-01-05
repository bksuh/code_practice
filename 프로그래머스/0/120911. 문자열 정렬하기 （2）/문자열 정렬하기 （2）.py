def solution(my_string):
    answer = [c.lower() for c in my_string]
    answer.sort()
    return ''.join(answer)