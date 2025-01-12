team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

result = [0 for _ in range(9)]
t1, t2, indi =  0, 0, False

for i in range(9):
    t1 += team1[i]
    if t1 > t2:
        indi = True
    t2 += team2[i]

print('Yes' if indi else 'No')