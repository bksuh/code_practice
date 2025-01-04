def solution(num_list):
    answer = [0, 0]
    for num in num_list:
        answer[num%2] += 1
    return answer