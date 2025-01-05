def solution(before, after):
    befo = [c for c in before]
    aft = [c for c in after]
    befo.sort()
    aft.sort()

    return 1 if befo == aft else 0