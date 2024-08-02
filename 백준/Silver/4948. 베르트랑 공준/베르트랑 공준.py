t = 123456
arr = [i for i in range(2*t+1)]
arr[1]= 0
for i in range(2, 2*t+1):
    for j in range(2*i, 2*t+1, i):
        arr[j]= 0
while True:
    t = int(input())
    if t == 0:
        break
    cnt = 0
    for i in range(t+1, 2*t+1):
        if arr[i] == 0:
            continue
        else:
            cnt += 1
    print(cnt)