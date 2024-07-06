case = 1
while True:
    a, b ,c = input().split()
    if b == 'E':
        break
    a, c = int(a), int(c)
    
    if b == '>':
        tmp = str(a>c).lower()
        print(f"Case {case}: {tmp}")
        case+=1
    elif b == '>=':
        tmp = str(a>=c).lower()
        print(f"Case {case}: {tmp}")
        case+=1
    elif b == '<':
        tmp = str(a<c).lower()
        print(f"Case {case}: {tmp}")
        case+=1
    elif b == '<=':
        tmp = str(a<=c).lower()
        print(f"Case {case}: {tmp}")
        case+=1
    elif b == '==':
        tmp = str(a==c).lower()
        print(f"Case {case}: {tmp}")
        case+=1
    else:
        tmp = str(a!=c).lower()
        print(f"Case {case}: {tmp}")
        case+=1
