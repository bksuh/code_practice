score = list(int(input()) for _ in range(8))
tmp=[]
for i, v in enumerate(score):
    tmp.append((i+1, v))
tmp.sort(key=lambda x: (-x[1]))
tmp1 =[]
for i in range(5):
    tmp1.append(tmp[i])
tmp1.sort(key= lambda x : x[0])
total = 0
ans =[]
for num, val in tmp1:
    total += val
    ans.append(num)
print(total)
print(*ans)    
