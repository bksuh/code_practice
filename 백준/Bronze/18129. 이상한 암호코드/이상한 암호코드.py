tar, t = input().split()
count = {}
tar = tar.upper()
for char in tar:
    if char not in count.keys():
        current = char
        count[current] = 0
    if char in count.keys() and current ==char:
        count[current] +=1
ans = ''
for counts in count.values():
    if counts >= int(t):
        ans += '1'
    else:
        ans += '0'
print(ans)