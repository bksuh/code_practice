n = int(input())
for _ in range(n):
    score = list(map(int, input().split()))
    score.sort()
    score.pop(0)
    score.pop(-1)
    if max(score)- min(score) >=4:
        print('KIN')
    else:
        print(sum(score))