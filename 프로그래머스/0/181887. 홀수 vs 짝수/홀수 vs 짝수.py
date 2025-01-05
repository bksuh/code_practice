def solution(num_list):
    a1, a2 = 0, 0
    for i in range(len(num_list)):
        if i%2 ==0:
            a1 += num_list[i]
        else:
            a2 += num_list[i]
    return max(a1, a2)