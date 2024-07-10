while True:
    a = input()
    if a =='0':
        break
    n, p = map(int, a.split())
    arr = []
    for i in range(n//4):
        arr.append([2*i+1, 2*i+2, -2*i+n-1, -2*i+n])
    for i in range(len(arr)):
        if p in arr[i]:
            ans = arr[i]
    ans.remove(p)
    print(*ans)
