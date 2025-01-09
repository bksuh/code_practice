t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    
    a_cnt = []
    b_cnt = []
    for i in range(1, 5):
        a_cnt.append((i, a.count(i)))
        b_cnt.append((i, b.count(i)))
    a_cnt.sort(key = lambda x : -x[0])
    b_cnt.sort(key = lambda x : -x[0])
    if a_cnt == b_cnt:
        print("D")
    elif a_cnt > b_cnt:
        print("A")
    else:
        print("B")