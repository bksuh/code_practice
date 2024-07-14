n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]
ans = []
for p in range(n):
    tmp = []
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                tmp.append((cards[p][i]+cards[p][j]+cards[p][k])%10)
    ans.append(tmp)

real = []
for i in range(len(ans)):
    real.append((i+1,max(ans[i])))
real.sort(key=lambda x:(-x[1], -x[0]))
print(real[0][0])