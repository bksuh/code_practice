picture = []
ans = ''
for _ in range(15):
    tmp = input().split()
    if 'w' in tmp:
        ans = 'chunbae'
    elif 'b' in tmp:
        ans = 'nabi'
    elif 'g' in tmp:
        ans = 'yeongcheol'
print(ans)