socks = []

for _ in range(5):
    socks.append(int(input()))

sock = set(socks)

for so in sock:
    if socks.count(so) %2 == 1:
        print(so)
        break