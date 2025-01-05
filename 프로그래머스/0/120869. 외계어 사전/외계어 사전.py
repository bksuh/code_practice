def solution(spell, dic):
    spell.sort()
    for word in dic:
        tmp = [c for c in word]
        tmp.sort()
        if spell == tmp:
            return 1
    return 2