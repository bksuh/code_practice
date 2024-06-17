n=int(input())
cnt =0
for _ in range(n):
    x = input()
    a=[]
    for i in range(len(x)):
        if (x[i] in a) and a[-1] !=x[i]:
            break
        a.append(x[i])
    if len(a) == len(x):
        cnt+=1
print(cnt)