def solution(num_list):
    answer = 0
    for num in num_list:
        cnt = 0
        while True:
            if num == 1:
                answer += cnt
                break
            if num% 2 == 0:
                num //= 2
            else:
                num = (num-1)//2
            cnt+=1
            
    return answer