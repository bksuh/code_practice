n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    ans = []
    while True:
        if a < b:
            ans.append(a)
            break
        ans.append(a%b)
        a = a//b
    if ans == ans[::-1]:
        print(1)
    else:
        print(0)