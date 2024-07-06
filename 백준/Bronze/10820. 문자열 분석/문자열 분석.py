while True:
    try:
        a = input()
        ans = [0, 0, 0, 0]
        for i in a:
            if i.isupper():
                ans[1]+=1
            elif i.islower():
                ans[0]+=1
            elif i.isdigit():
                ans[2]+=1
            elif i == ' ':
                ans[3]+=1
        print(*ans)
    except:
        break