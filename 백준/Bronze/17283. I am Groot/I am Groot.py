import math

l = int(input())
r = int(input())
tmp = math.floor(l*(r/100))
trees = [tmp]
while tmp > 5:
    tmp = math.floor(tmp*(r/100))
    trees.append(tmp)
trees = trees[:len(trees)-1]
ans = 0
for i, v in enumerate(trees):
    ans += pow(2, i+1)*v
print(ans)