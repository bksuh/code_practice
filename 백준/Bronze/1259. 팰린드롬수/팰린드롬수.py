while True:
    a = list(int(c) for c in input())
    if a == [0]:
        break
    b = list(reversed(a))

    if a == b:
        print("yes")
    else:
        print('no')