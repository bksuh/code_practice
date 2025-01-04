def solution(myString):
    answer = ''
    for c in myString:
        if c =='a':
            c = c.upper()
        elif c.isupper() and c != 'A':
            c = c.lower()
        answer +=c
    return answer