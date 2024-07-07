a = input()
h = a.count(':-)')
s = a.count(':-(')

if h==0 and s==0:
    print('none')
elif h == s:
    print('unsure')
elif h>s:
    print('happy')
else:
    print('sad')