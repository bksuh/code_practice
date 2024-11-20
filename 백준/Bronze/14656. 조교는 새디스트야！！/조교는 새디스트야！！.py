t = int(input())
lines = list(map(int, input().split()))

cnt = 0

for i in range(t):
    if lines[i] != i+1:
        cnt+=1
print(cnt)