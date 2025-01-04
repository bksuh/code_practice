def solution(my_string):
    upper_list = [0 for _ in range(ord('Z')-ord('A')+1)]
    lower_list = [0 for _ in range(ord('z')-ord('a')+1)]

    for c in my_string:
        if c.isupper():
            upper_list[ord(c)-ord('A')] += 1
        else:
            lower_list[ord(c)-ord('a')] +=1
    answer = upper_list+lower_list

    return answer