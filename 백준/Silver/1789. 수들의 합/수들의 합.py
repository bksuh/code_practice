n = int(input())
tmp = 0
cnt = 0

for i in range(1, n):
    tmp += i
    if tmp >n:
        break
    cnt +=1
    
if n == 1:
    print(1)
else:
    print(cnt)