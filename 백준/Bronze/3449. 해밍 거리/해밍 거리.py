n = int(input())
for _ in range(n):
    ham = 0
    a = input()
    b = input()
    for i in range(len(a)):
        if a[i] != b[i]:
            ham += 1
    print(f"Hamming distance is {ham}.")