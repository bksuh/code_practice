t = int(input())

for _ in range(t):
    a = input()
    ans = 0
    for c in a:
        if c == ' ':
            continue
        tmp = ord(c) - ord("A") + 1
        ans += tmp
    if ans == 100:
        print("PERFECT LIFE")
    else:
        print(ans)