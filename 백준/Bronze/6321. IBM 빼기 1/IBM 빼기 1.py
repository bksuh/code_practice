n = int(input())
for i in range(n):
    string = input()
    ans =''
    for c in string:
        if c =='Z':
            ans+='A'
        else:
            ans+=chr(ord(c)+1)
    print(f"String #{i+1}")
    print(ans)
    print()