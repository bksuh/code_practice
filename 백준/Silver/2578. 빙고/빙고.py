picks = [list(map(int, input().split())) for _ in range(5)]
calls = []
for _ in range(5):
    tmp = list(map(int, input().split()))
    calls.extend(tmp)

ans = [0, 0, 0, 0, 0]
for i in range(len(calls)):
    bingo = []
    call = calls[i]
    for j in range(len(picks)):
        if call in picks[j]:
            picks[j][picks[j].index(call)] = 0
        bingo.append(picks[j])
    for k in range(5):
        tmp = [picks[0][k], picks[1][k], picks[2][k], picks[3][k], picks[4][k]]
        bingo.append(tmp)
    tmp = [picks[0][0], picks[1][1], picks[2][2], picks[3][3], picks[4][4]]
    bingo.append(tmp)
    tmp = [picks[4][0], picks[3][1], picks[2][2], picks[1][3], picks[0][4]]
    bingo.append(tmp)
    if bingo.count(ans) >= 3:
        print(i+1)
        break