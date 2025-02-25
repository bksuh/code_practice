t = int(input())
s = input()

ans = ''

for c in s:
    if c == 'l':
        ans += 'L'
    else:
        ans += 'i'
    
print(ans)