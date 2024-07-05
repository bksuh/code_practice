cnt = 0
for i in range(8):
    stat = input()
    for j in range(8):
        if i%2==0 and j%2==0 and stat[j]=='F':
            cnt +=1
        if i%2==1 and j%2==1 and stat[j]=='F':
            cnt+=1
print(cnt)