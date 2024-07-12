n =int(input())
tar = input()
t = len(tar)
ans =[]
for i in range(t//n):
    if i%2 ==0:
        ans.append(tar[n*i:n*i+n])
    else:
        ans.append(tar[n*i+n-1:n*i-1:-1])

for i in range(n):
    for element in ans:
        print(element[i], end='')