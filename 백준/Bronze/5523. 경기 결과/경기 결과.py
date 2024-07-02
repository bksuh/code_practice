n = int(input())
score_a, score_b = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a> b :
        score_a +=1
    elif a < b:
        score_b += 1
print( score_a, score_b)