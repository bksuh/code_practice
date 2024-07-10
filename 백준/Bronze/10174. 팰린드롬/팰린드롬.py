n = int(input())
for _ in range(n):
    string = input().lower()
    if string == string[::-1]:
        print('Yes')
    else:
        print('No')