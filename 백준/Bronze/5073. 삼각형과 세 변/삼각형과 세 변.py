while True:
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        tmp =[a,b,c]
        tmp.sort()
        if tmp[-1] >= tmp[0]+tmp[1]:
            print("Invalid")
            continue
        a = set(tmp)
        if len(a) ==3:
            print("Scalene")
        elif len(a) ==2:
            print("Isosceles")
        else:
            print("Equilateral")