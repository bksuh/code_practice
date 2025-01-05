def solution(age):
    answer = ''
    ages = [int(c) for c in str(age)]
    for ag in ages:
        answer += chr(ord('a')+ag)
    return answer