n = int(input())
tmp = list(str(i) for i in range(1, n+1))
ans = ''.join(tmp)
print(ans.index(str(n))+1)