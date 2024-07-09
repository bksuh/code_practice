ans = int(input())

while True:
    b = input()
    if b == "=":
        break
    a = int(input())
    if b == '+':
        ans +=a
    elif b =='-':
        ans -= a
    elif b == '*':
        ans *=a
    else:
        ans //=a
print(ans)