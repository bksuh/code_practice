def solution(str_list, ex):
    answer = ''
    for str1 in str_list:
        if ex in str1:
            continue
        else:
            answer += str1
    return answer