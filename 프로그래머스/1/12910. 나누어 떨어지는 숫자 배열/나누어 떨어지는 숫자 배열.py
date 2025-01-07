def solution(arr, divisor):
    answer = []
    for elem in arr:
        if elem % divisor == 0:
            answer.append(elem)
    answer.sort()
    return answer if len(answer) != 0 else [-1]