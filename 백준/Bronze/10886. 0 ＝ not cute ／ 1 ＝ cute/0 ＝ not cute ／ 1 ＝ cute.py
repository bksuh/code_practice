n = int(input())
cnt = 0
for _ in range(n):
    a = int(input())
    if a==1:
        cnt+=1
    else:
        cnt-=1

if cnt > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")