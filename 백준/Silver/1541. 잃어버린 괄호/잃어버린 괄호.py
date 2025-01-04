a =  input().split('-')
num = []

for i in a:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)
start = num[0]
for i in range(1, len(num)):
    start -= num[i]
print(start)