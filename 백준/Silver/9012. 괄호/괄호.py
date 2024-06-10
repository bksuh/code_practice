n = int(input())
for _ in range(n):
    string = input()
    result = 0
    flag = False
    for element in string:
        if element =='(':
            result +=1
        elif element ==')':
            result -=1
        if result == 0 and element=='(':
            flag = True
            break
    if flag:
        print('NO')
    elif result==0:
        print('YES')
    else:
        print('NO')