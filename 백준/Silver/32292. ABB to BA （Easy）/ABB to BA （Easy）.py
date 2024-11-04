t = int(input())
tar = 'ABB'
for _ in range(t):
    a = int(input())
    b = input()
    while tar in b:
        b = b.replace(tar, 'BA')
    print(b)