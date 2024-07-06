a = int(input())
while True:
    b = int(input())
    if not b:
        break
    if b%a == 0:
        print(f"{b} is a multiple of {a}.")
    else:
        print(f"{b} is NOT a multiple of {a}.")