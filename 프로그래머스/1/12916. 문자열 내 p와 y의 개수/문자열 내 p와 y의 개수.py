def solution(s):
    answer = True
    s = s.lower()
    if s.count('p') == 0 and s.count('y') == 0:
        return True
    elif s.count('p') == s.count('y'):
        return True
    else:
        return False