a , b = input().split()
mina, minb, maxa, maxb = '', '', '',''
for c in a:
    if c == '5' or c == '6':
        mina+='5'
        maxa+='6'
    else:
        mina+=c
        maxa+=c

for d in b:
    if d == '5' or d == '6':
        minb +='5'
        maxb +='6'
    else:
        minb+=d
        maxb+=d

print(int(mina)+int(minb), int(maxa)+int(maxb))

