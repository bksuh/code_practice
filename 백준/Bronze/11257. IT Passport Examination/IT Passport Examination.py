t = int(input())

for _ in range(t):
    id, a, b, c = map(int, input().split())
    if a+b+c >= 55 and a >= 35*0.3 and b>= 25*0.3 and c >=40*0.3:
        print(f"{id} {a+b+c} PASS")
    else:
        print(f"{id} {a+b+c} FAIL")