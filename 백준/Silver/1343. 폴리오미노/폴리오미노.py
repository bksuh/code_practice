tar = list(input().split('.'))
ans = ''
for elem in tar:
    if len(elem) % 2 == 1:
        ans = -1
        break
    a = len(elem) // 4
    b  = (len(elem) % 4)//2
    ans += 'AAAA'*a
    ans += 'BB'*b
    ans += '.'
if ans == -1:
    print(-1)
else:
    print(ans[:len(ans)-1])