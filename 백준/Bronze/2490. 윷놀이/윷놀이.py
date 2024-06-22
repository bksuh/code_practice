d = {0:'D', 1:'C', 2:'B', 3:'A', 4:'E'}

for _ in range(3):
    arr = list(map(int, input().split()))
    print(d[arr.count(1)])