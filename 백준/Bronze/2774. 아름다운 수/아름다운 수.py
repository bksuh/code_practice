n = int(input())
for _ in range(n):
    a = input()
    tmp = list(int(c) for c in a)
    tmp = set(tmp)
    print(len(tmp))