mbti = input()

ans = ''
for c in mbti:
    if c =='E':
        ans+='I'
    elif c =='I':
        ans+='E'
    elif c =='F':
        ans+='T'
    elif c =='T':
        ans+='F'
    elif c =='S':
        ans+='N'
    elif c =='N':
        ans+='S'
    elif c =='J':
        ans+='P'
    else:
        ans+='J'
print(ans)