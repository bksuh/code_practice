a = int(input())
five = a//5
three = a//3
arr=[]
for i in range(five+1):
    for j in range(three+1):
        if 5*i + 3*j != a:
            pass
        else:
            arr.append(i+j)
if len(arr)==0:
    print(-1)
else:
    print(min(arr))