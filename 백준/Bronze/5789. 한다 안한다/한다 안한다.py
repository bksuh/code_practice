n = int(input())
for _ in range(n):
    a = input()
    if a[len(a)//2] == a[(len(a)//2)-1]:
        print("Do-it")
    else:
        print('Do-it-Not')