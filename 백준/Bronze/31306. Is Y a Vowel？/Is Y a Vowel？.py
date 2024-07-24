arr = ['a', 'e', 'i', 'o','u']
tar = input()
cnt, cnt1 = 0, 0
for c in tar:
    if c in arr:
        cnt+=1
        cnt1+=1
    if c == 'y':
        cnt1+=1
print(cnt, cnt1)