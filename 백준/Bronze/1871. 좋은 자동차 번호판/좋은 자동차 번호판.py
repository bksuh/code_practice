n = int(input())

for _ in range(n):
    a, b = input().split('-')
    total = 0
    for i in range(3):
        total += (ord(a[i])-ord('A'))*pow(26,2-i)
    ans = total - int(b)
    print("nice" if abs(ans)<=100 else "not nice")