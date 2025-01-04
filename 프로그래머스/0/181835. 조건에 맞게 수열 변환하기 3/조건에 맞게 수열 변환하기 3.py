def solution(arr, k):
    answer = []
    if k% 2 == 1:
        for i in range(len(arr)):
            answer.append(k*arr[i])
    else:
        for i in range(len(arr)):
            answer.append(k+arr[i])
    return answer