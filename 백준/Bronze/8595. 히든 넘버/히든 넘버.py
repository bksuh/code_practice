n = int(input())
string = input()
ans = 0
tmp = ''
for c in string:
    if c.isdigit():
        tmp += c
    else:
        if tmp != '':
            ans += int(tmp)
        tmp = ''
if tmp != '':
    ans += int(tmp)
print(ans)