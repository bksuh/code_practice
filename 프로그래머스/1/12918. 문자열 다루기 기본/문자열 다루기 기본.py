def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try:
            a = int(s)
            return True
        except:
            return False
    return False