a, b = map(int, input().split())
arr=[]
tmp = 1
for _ in range(b):
    while True:
        if tmp == arr.count(tmp):
            break
        arr.append(tmp)
        if len(arr) >b:
            break
    tmp +=1
    if len(arr) > b:
        break
ans = arr[a-1:b]

print(sum(ans))