def solution(str_list):
    answer = []
    idx = 0
    for c in str_list:
        if c =='l':
            idx = str_list.index(c)
            return str_list[:idx]
        elif c == 'r':
            idx = str_list.index(c)
            return str_list[idx+1:]
    return answer