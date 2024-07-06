a = list(input())
x, y = 0, 0
for i in range(len(a)-2):
    tmp = a[i]+a[i+1]+a[i+2]
    if tmp == 'JOI':
        x+=1
    elif tmp =='IOI':
        y+=1
print(x)
print(y)