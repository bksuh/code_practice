n = 5
arr=[]
for _ in range(n):
    a = int(input())
    if a>=40:
        arr.append(a)
    else:
        arr.append(40)

print(sum(arr)//len(arr))