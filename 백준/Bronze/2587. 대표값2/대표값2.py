score = list(int(input()) for _ in range(5))
print(int(sum(score)/len(score)))
score.sort()
print(score[2])