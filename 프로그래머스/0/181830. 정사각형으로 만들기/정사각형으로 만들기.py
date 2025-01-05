def solution(arr):
    n = len(arr)
    m = len(arr[0])
    real = max(n, m)
    if n == m:
        return arr
    elif n > m:
        answer = []
        for elem in arr:
            for _ in range(n-m):
                elem.append(0)
            answer.append(elem)
        return answer
    else:
        answer = arr
        for _ in range(m-n):
            answer.append([0 for _ in range(m)])
                
    return answer