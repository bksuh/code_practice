ans = input()
n = int(input())
tmp = []
for _ in range(n):
    a = input()
    indi = True
    for i in range(len(a)):
        if ans[i] == '*':
            continue
        elif ans[i] != a[i]:
            indi = False
            break
    if indi:
        tmp.append(a)

print(len(tmp))
print(*tmp, sep='\n')