while True:
    a = input()
    if a == 'EOI':
        break
    a = a.lower()
    print("Found" if 'nemo' in a else "Missing")