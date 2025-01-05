def solution(my_string):
    answer = []
    my_string = my_string.strip(' ').split()
    for elem in my_string:
        answer.append(elem.strip(' '))
    

    return answer