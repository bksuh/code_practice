def solution(A, B):
    answer = 10000
    indi = False
    for i in range(len(A)):
        tmp = A[len(A)-i:] + A[:len(A)-i]
        print(tmp)
        if tmp == B:
            answer = min(answer, i)
            indi = True
    if indi:
        return answer
    else:
        return -1