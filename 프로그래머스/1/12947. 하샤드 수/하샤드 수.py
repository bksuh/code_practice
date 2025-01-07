def solution(x):

    tmp = [int(c) for c in str(x)]
    if x % sum(tmp) == 0:
        return True
    return False