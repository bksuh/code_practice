n = int(input())
if n == 0:
    print("divide by zero")
else:
    arr = list(map(int, input().split()))
    avg = sum(arr) / n
    keys = set(arr)
    tmp = 0
    for key in keys:
        tmp += (arr.count(key)/n)*key
    ans = avg / tmp
    print(f"{ans:.2f}")