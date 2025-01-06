def solution(numlist, n):
    answer = []
    for num in numlist:
        answer.append((num, abs(num-n)))
    answer.sort(key=lambda x: (x[1], -x[0]))
    real = []
    for a, b in answer:
        real.append(a)
    return real