def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += (i+1)*price
    if answer - money >= 0:
        return answer - money
    return 0