a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, y=0,0
for i in range(len(a)):
    if a[i] == b[i]:
        continue
    elif a[i]>b[i]:
        x+=1
    else:
        y+=1
if x>y:
    print('A')
elif x<y:
    print('B')
else:
    print('D')