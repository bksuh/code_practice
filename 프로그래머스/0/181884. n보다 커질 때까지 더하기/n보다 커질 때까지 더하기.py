def solution(numbers, n):
    answer = 0
    for nums in numbers:
        answer += nums
        if answer > n:
            break
    return answer