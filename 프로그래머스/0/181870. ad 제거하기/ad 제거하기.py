def solution(strArr):
    answer = []
    for string in strArr:
        if 'ad' in string:
            continue
        else:
            answer.append(string)
    return answer