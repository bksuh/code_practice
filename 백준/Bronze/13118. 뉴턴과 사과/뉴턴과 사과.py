peoples = list(map(int, input().split()))
x, y, r = map(int, input().split())
indi = False

for idx, p in enumerate(peoples):
    if p == x:
        indi = True
        print(idx + 1)
        break

if not indi:
    print(0)