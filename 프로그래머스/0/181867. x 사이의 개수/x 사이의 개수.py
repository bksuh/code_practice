def solution(myString):
    tmp = myString.split('x')
    answer = []
    for elem in tmp:
        answer.append(len(elem))

    return answer