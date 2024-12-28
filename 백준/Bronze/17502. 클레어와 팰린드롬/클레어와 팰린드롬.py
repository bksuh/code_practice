t = int(input())
string = input()

if t == string.count('?'):
    print('a'*t)
else:
    tmp = string[::-1]
    ans = ''
    for i in range(len(tmp)):
        if string[i] == '?' and tmp[i] !='?':
            ans+=tmp[i]
        elif string[i] != '?' and tmp[i] == '?':
            ans+=string[i]
        elif string[i] == '?' and  tmp[i] =='?':
            ans +='a'
        else:
            ans+=tmp[i]
            
    print(ans)