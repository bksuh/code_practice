arr = []
s = input()
for i in range(len(s)):
    arr.append(s[i:])
arr.sort()
for elem in arr:
    print(elem)