arr=[]
for i in range(5):
    a = input()
    if 'FBI' in a:
        arr.append(i+1)
if arr:
    print(*arr)
else:
    print('HE GOT AWAY!')
    