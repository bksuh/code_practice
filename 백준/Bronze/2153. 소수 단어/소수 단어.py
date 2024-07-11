target = input()
ans = 0
for c in target:
    if c.isupper():
        ans += ord(c)-ord('A') + 27
    else:
        ans += ord(c) - ord('a') + 1
indi = True

for i in range(2, ans):
    if ans%i == 0:
        indi = False
        break
if indi:
    print("It is a prime word.")
else:
    print("It is not a prime word.")