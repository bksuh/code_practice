n = int(input())
scores = []
contries = []
for _ in range(n):
    a = tuple(map(int,input().split()))
    scores.append(a)
scores.sort(key=lambda x: -x[2])
cnt = 0
for con, stu, score in scores:
    if contries.count(con) == 2:
        continue
    if cnt == 3:
        break
    print(con, stu)
    contries.append(con)
    cnt+=1