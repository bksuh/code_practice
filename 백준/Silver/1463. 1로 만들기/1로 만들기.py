t = int(input())
arr = [i for i in range(t+1)]
arr[1] = 0
for k in range(2, t+1):
    tmp = [arr[k-1]+1]
    if k%2 == 0:
        a = arr[k//2] + 1
        tmp.append(a)
    if k%3 == 0:
        b = arr[k//3] + 1
        tmp.append(b)


    arr[k] = min(tmp)
print(arr[t])