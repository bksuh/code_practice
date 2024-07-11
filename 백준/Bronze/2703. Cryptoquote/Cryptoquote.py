n = int(input())

for _ in range(n):
    tar = input()
    dic = list(input())
    ans = ''
    for c in tar:
        if c == ' ':
            ans += ' '
            continue
        ans += dic[ord(c)-ord('A')]
    print(ans)