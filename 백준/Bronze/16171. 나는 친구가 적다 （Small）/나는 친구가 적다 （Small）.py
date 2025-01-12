s = input()
real = ''
for c in s:
    if c.isalpha():
        real += c
sear = input()
print(1 if sear in real else 0)