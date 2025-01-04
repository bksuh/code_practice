def solution(myString, pat):
    answer = ''
    for c in myString:
        if c =='A':
            answer += 'B'
        else:
            answer += 'A'
    if pat in answer:
        return 1
    return 0