import math

cnt = 1
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if a == -1:
        line = 'a'
        length = float(c)**2 - float(b)**2
        if length <=0:
            length = -1
        else:
            length = (float(c)**2 - float(b)**2) **(1/2)
    elif b == -1:
        line = 'b'
        length = float(c)**2 - float(a)**2
        if length <= 0:
            length = -1
        else:
            length = (float(c)**2 - float(a)**2) **(1/2)
    elif c == -1:
        line = 'c'
        length = (float(a)**2 + float(b)**2) **(1/2)
    print(f"Triangle #{cnt}")
    if float(length) <=0 :
        print("Impossible.")
    else:
        print(f"{line} = {length:.3f}")
    print()
    cnt+=1
    
    