def solution(my_string, queries):
    answer = ''
    for s, e in queries:
        tmp = my_string[s:e+1]
        my_string = my_string[:s] + tmp[::-1] + my_string[e+1:]
    return my_string