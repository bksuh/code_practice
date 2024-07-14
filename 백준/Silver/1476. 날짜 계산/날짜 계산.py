a, b, c = map(int, input().split())
e, s, m = 1,1, 1
ans = 1
while True:
    if a==e and b ==s and m == c:
        break
    e += 1
    s += 1
    m += 1
    ans +=1
    if e >= 16:
        e = 1
    if s >= 29:
        s =1
    if m >= 20:
        m = 1
print(ans)