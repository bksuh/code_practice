kid = list(int(input()) for _ in range(9))
tmp = kid
indi = False
for i in range(9):
    for j in range(i, 9):
        if i==j:
            continue
        if sum(kid) - kid[i] -kid[j] == 100:
            indi = True
            kid.pop(j)
            break
    if indi:
        kid.pop(i)
        break
for elem in kid:
    print(elem)