def solution(my_string):
    answer = []
    for c in my_string:
        if c.isdigit():
            answer.append(int(c))
    answer.sort()
    return answer