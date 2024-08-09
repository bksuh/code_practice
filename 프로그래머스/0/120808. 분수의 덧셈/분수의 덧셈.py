def solution(numer1, denom1, numer2, denom2):
    answer = []
    tmp = numer1*denom2 + numer2*denom1
    tmp2 = denom1*denom2
    for i in range(1, min(tmp, tmp2)+1):
        if tmp%i == 0 and tmp2%i == 0:
            ans = i
    answer.append(tmp//ans)
    answer.append(tmp2//ans)
    return answer