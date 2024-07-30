n = int(input())
start, end = input().split('*')
st = len(start)
et = len(end)
for _ in range(n):
    tmp = input()
    if tmp[0:st] == start and tmp[len(tmp)-et:] == end and len(tmp)>=st+et:
        print("DA")
    else:
        print('NE')