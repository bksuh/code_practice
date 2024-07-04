h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

h, m, s = h2-h1, m2-m1, s2-s1

if s<0:
    s+=60
    m-=1
if m<0:
    m+=60
    h-=1
if h<0:
    h+=24
ans = [h,m,s]
for i in range(len(ans)):
    elem = str(ans[i])
    if len(elem) == 1:
        elem = '0'+ elem
    if i==2:
        print(elem)
    else:
        print(elem, end=':')
