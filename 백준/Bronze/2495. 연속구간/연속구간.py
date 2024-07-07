for _ in range(3):
    a = input()
    arr = [int(c) for c in a]
    cnt = 1
    cur = arr[0]
    tmp =[]
    for i in range(1,len(arr)):
        if cur == arr[i]:
            cnt +=1
        else:
            tmp.append(cnt)
            cnt = 1
            cur = arr[i]
    tmp.append(cnt)
    print(max(tmp))