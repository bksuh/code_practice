n, m = map(int, input().split())
tmp = list(map(int, input().split()))
score ={}
result = []
for k,v in enumerate(tmp):
    score[k] = v
for _ in range(m):
    tmp = list(input().split())
    ans = 0
    for i in range(1, len(tmp)):
        if tmp[i] == 'O':
            ans += score[i-1]
    
    result.append((int(tmp[0]), ans))
result.sort(key=lambda x:(-x[1],x[0]))
print(*result[0])