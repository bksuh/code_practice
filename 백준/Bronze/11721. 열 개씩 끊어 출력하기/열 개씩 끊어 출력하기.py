target = input()
cnt = 0
for i in target:
    print(i, end='')
    cnt+=1
    if cnt==10:
        print()
        cnt=0