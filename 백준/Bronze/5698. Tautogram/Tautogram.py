while True:
    sting = list(input().lower().split())
    if sting == ['*']:
        break
    indi = True
    for i in range(len(sting)-1):
        if sting[i][0] != sting[i+1][0]:
            indi = False
    print('Y' if indi else 'N')