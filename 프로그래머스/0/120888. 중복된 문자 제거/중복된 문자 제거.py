def solution(my_string):
    answer = ''
    for c in my_string:
        if c in answer:
            continue
        answer+=c
    return answer