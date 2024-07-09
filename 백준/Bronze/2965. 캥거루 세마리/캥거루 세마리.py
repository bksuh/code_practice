a, b, c = map(int, input().split())
cnt = 0
while True:
    len_left = b-a-1
    len_right = c-b-1

    if len_left ==0 and len_right==0:
        break
    if len_left < len_right:
        tmp = c-1
        a = b
        b= tmp
    else:
        tmp = a+1
        c=b
        b= tmp
    cnt+=1
print(cnt)