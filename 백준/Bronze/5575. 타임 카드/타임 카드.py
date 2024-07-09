for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    ha, ma, sa = h2-h1, m2-m1, s2-s1
    if sa< 0:
        ma-=1
        sa+=60
    if ma < 0:
        ha-=1
        ma+=60
    print(ha, ma, sa)