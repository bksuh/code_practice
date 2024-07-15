n, m = map(int, input().split())
cards = []
for _ in range(n):
    tmp = sorted(list(map(int, input().split())), reverse= True)
    cards.append(tmp)
ans =[]
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(cards[j][i])
    ans.append(tmp)
scores =[0]*n

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] == max(ans[i]):
            scores[j] += 1

for i in range(len(scores)):
    if scores[i] == max(scores):
        print(i+1, end =' ')