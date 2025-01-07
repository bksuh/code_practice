a = input()
b = input()
pick = ''
for i in range(len(a)):
    pick += a[i]
    pick += b[i]

while len(pick) >= 3:
    ans = ''
    for i in range(0, len(pick)-1):
        ans += str(int(pick[i]) + int(pick[i+1]))[-1]

    pick = ans
print(pick)