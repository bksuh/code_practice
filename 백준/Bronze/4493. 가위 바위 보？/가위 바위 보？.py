n = int(input())

for _ in range(n):
    t = int(input())
    a, b = 0, 0
    for _ in range(t):
        x, y = input().split()
        if x =="R":
            if y=='S':
                a+=1
            elif y=='P':
                b+=1
            else:
                continue
        elif x=='S':
            if y =='P':
                a+=1
            elif y== 'R':
                b+=1
            else:
                continue
        else:
            if y=='R':
                a+=1
            elif y=='S':
                b+=1
            else:
                continue
    if a>b:
        print("Player 1")
    elif a<b:
        print("Player 2")
    else:
        print('TIE')