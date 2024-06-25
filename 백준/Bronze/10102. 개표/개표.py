n = int(input())
result = input()

a = result.count('A')
b = result.count('B')

if a>b:
    print('A')
elif a==b:
    print('Tie')
else:
    print('B')