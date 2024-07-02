tmp = input()
if len(tmp) >=2:
    a, b  = int(tmp[0]), int(tmp[1])
else:
    a,b= 0, int(tmp[0])

cnt=0
indi = False
while True:
    if indi:
        break
    result = a + b
    if str(10*a + b) == tmp and cnt != 0:
        indi = True
    cnt+=1
    a = b
    b = result%10
print(cnt-1)
