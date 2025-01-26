while True:
    t = int(input())
    if t == 0:
        break
    elif t%42 == 0:
        print('PREMIADO')
    else:
        print('TENTE NOVAMENTE')