a= int(input())
b= int(input())
ans = []
for i in range(a, b+1):
    tmp =[]
    for j in range(1, i+1):
        if i%j ==0:
            tmp.append(j)
        if len(tmp) >=3:
            break
    if len(tmp) ==2:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
