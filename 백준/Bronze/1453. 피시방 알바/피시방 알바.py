seat = [False for _ in range(101)]
n = int(input())
c = list(map(int, input().split()))

cnt = 0
for a in c:
    if seat[a] == True:
        cnt +=1
    else:
        seat[a] = True

print(cnt)