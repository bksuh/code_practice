a = input()
ans = 1

for i in range(len(a)-1):
    if ord(a[i]) >= ord(a[i+1]):
        ans += 1
print(ans)