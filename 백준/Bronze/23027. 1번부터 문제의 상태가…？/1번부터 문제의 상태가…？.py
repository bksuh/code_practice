s = input()

if 'A' in s:
    for elem in ['B', 'C', 'D', 'F']:
        s = s.replace(elem, 'A')
elif 'B' in s:
    for elem in ['C', 'D', 'F']:
        s = s.replace(elem, 'B')
elif 'C' in s:
    for elem in ['D', 'F']:
        s = s.replace(elem, 'C')
else:
    s = 'A'*(len(s))

print(s)