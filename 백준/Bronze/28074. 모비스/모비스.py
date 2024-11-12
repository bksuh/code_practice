a = [c for c in input()]
ca = [c for c in 'MOBIS']

for c in a:
    if c in ca:
        ca.remove(c)

print("NO" if ca else "YES")