h1, m1, s1 = map(int,input().split(':'))
h2, m2, s2 = map(int,input().split(':'))

h3, m3, s3 = h2-h1, m2-m1, s2-s1

if s3 < 0:
    m3-=1
    s3+=60
if m3 < 0:
    h3-=1
    m3+=60
if h3 < 0:
    h3+=24
tmp = [h3,m3,s3]
ans =''
for element in tmp:
    if len(str(element)) == 1:
        ans += '0'+str(element)
    else:
        ans+=str(element)
    ans +=':'
if ans[:len(ans)-1] =='00:00:00':
    print('24:00:00')
else:
    print(ans[:len(ans)-1])
