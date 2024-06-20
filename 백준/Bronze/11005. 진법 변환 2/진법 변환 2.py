a, b = map(int, input().split())

d = {}
for i in range(0, b):
    if i>=10:
        d[i] = chr(55+i)
    else:
        d[i]= str(i)
arr =[]

while True:
    if a == 0:
        break
    remain = a%b
    arr.append(d[remain])
    a = a//b

for element in reversed(arr):
    print(element, end ='')