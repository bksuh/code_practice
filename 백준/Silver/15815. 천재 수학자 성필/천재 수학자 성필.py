tar = input()
arr = []

for c in tar:
    if c.isdigit():
        arr.append(int(c))
    if c == '-':
        a1 = arr.pop()
        a2 = arr.pop()
        arr.append(a2-a1)
    elif c == '+':
        a1 = arr.pop()
        a2 = arr.pop()
        arr.append(a2+a1)
    elif c == '*':
        a1 = arr.pop()
        a2 = arr.pop()
        arr.append(a2*a1)
    elif c == '/':
        a1 = arr.pop()
        a2 = arr.pop()
        arr.append(a2//a1)

print(arr[0])