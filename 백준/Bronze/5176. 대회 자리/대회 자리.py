n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr =[]
    cnt = 0
    for i in range(a):
        t = input()
        if t in arr:
            cnt+=1
            continue
        else:
            arr.append(t)
    print(cnt)