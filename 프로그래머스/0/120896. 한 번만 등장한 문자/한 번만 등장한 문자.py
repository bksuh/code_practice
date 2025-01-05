def solution(s):
    tmp = []
    for c in s:
        if s.count(c) == 1:
            tmp.append(c)
    tmp.sort()
    return ''.join(tmp)