a = int(input())

ans = []
while True:
    if a == 1:
        break
    tmp = []
    for i in range(1, a+1):
        if a%i == 0:
            tmp.append(i)
        if len(tmp) ==2:
            break
    
    ans.append(tmp[-1])
    a //=tmp[-1]
ans = sorted(ans)
for element in ans:
    print(element)