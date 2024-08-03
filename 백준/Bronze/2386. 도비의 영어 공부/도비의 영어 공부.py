while True:
    tmp = input()
    if tmp == '#':
        break
    tar = tmp[0]
    rest = tmp[2::].lower()

    print(tar, rest.count(tar))