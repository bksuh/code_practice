i = 1
while True:
    a = input()
    b = input()
    if a=='END' and b=='END':
        break
    a1 = list(a)
    a1.sort()
    b1 = list(b)
    b1.sort()
    print(f"Case {i}: ", end ='')
    print('same' if a1==b1 else 'different')
    i+=1