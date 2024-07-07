start = float(input())
while True:
    tmp = float(input())
    if tmp == 999:
        break
    print(f"{tmp-start:.2f}")
    start = tmp
