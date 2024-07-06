a, b = input().split()
ans = ''
for i in range(int(a)):
    ans+=a

if len(ans)> int(b):
    print(ans[:int(b)])
else:
    print(ans)