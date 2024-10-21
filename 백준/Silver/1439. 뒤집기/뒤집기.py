a = input()
z, o = 0, 0

start = a[0]
for i in range(1, len(a)):
    if a[i] != start and start=='0':
        start = '1'
        z +=1
    elif a[i] != start and start=='1':
        start = '0'
        o+=1
if a[i] == '1':
    o += 1
else:
    z += 1
print(min(z, o))