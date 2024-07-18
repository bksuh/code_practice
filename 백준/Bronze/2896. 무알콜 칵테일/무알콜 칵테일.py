a,b,c = map(int, input().split())
i,j,k = map(int, input().split())

i1,j1, k1 = a/i, b/j, c/k
tmp = min(i1, j1, k1)
ans = [a-tmp*i, b-tmp*j, c-tmp*k]
for elem in ans:
    if elem == int(elem):
        print(int(elem), end=' ')
    else:
        print(f"{elem:.6f}", end=' ')
