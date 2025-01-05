def solution(emergency):
    answer = []
    real = sorted(emergency)[::-1]
    lookup = {}
    for i,v in enumerate(real):
        lookup[v] = i+1
    for emer in emergency:
        answer.append(lookup[emer])
    return answer