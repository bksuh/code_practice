t = int(input())

for _ in range(t):
    ans = 0
    tmp = input()
    a = int(input())
    for _ in range(a):
        ans += int(input())
    if ans%a == 0:
        print("YES")
    else:
        print("NO")