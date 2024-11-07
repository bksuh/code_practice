while True:
    try:
        a = input()
        while 'BUG' in a:
            a = a.replace('BUG','')
        print(a)
    except:
        break