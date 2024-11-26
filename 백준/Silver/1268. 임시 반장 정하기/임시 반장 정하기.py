t = int(input())
votes = [0] * t
info = []

for i in range(t):
    tmp = list(map(int, input().split()))
    info.append(tmp)
    votes[i] = [0]*t
    
for i in range(5):
    for j in range(t):
        for k in range(j+1, t):
            if info[j][i] == info[k][i]:
                votes[k][j] = 1
                votes[j][k] = 1
ans = []
for vote in votes:
    ans.append(vote.count(1))
print(ans.index(max(ans))+1)
