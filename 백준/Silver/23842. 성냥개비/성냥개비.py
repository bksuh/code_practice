total = int(input())
counts = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

def count1(value, version='cnt'):
    if version == 'cnt':
        return sum(counts[int(c)] for c in str(value)) + (6 if value < 10 else 0)
    elif version == 'string':
        return f"{value:02}"

def solution(total):
    for i in range(100):
        for j in range(100):
            k = i + j
            if len(str(k)) >= 3:
                continue
            tmp = count1(i) + 4 + count1(j) + count1(k)
            if tmp == total:
                return f"{count1(i, 'string')}+{count1(j, 'string')}={count1(k, 'string')}"
    return 'impossible'

print(solution(total))
