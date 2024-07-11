while True:
    target = input()
    if target == '0':
        break
    tmp = list(map(int, target.split()))[1:]
    ans = [tmp[0]]
    for i in range(1, len(tmp)):
        if ans[-1] == tmp[i]:
            continue
        ans.append(tmp[i])
    print(*ans, end =' $\n')