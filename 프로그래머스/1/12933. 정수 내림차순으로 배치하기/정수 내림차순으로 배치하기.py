def solution(n):
    answer = [c for c in str(n)]
    answer.sort(reverse=True)
    
    return int(''.join(answer))