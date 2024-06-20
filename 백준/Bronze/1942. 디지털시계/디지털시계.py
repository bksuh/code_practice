for _ in range(3):
    a, b = input().split()
    a= int(a.replace(':', ''))
    b= int(b.replace(':', ''))
    if a >b:
        b+=240000
    cnt = 0
    for i in range(a, b+1):
        i_sec = i%100
        i_min = ((i-i_sec)//100)%100
        i_hr = i//10000
        if i%3 == 0 and i_sec <=59 and i_min <=59:
            cnt += 1
    print(cnt)