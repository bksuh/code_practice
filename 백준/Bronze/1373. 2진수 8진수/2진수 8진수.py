digit = [int(c) for c in input()]
digit.reverse()

cnt, total = 0, 0
ans=[]
for i in range(len(digit)):
    if cnt ==3:
        cnt = 0
        ans.append(total)
        total = 0
    total += digit[i]*pow(2, cnt)
    cnt+=1
    if i == len(digit)-1:
        ans.append(total)
for i in reversed(ans):
    print(i, end='')
    