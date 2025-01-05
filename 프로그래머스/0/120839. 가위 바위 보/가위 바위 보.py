def solution(rsp):
    answer = ''
    for pick in rsp:
        if pick == '2':
            answer += '0'
        elif pick == '0':
            answer += '5'      
        else:
            answer += '2'
    return answer