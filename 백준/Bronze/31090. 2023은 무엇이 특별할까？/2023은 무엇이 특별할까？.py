t = int(input())

for _ in range(t):
    year = input()
    div = year[2:]
    if (int(year)+1)%int(div)==0:
        print("Good")
    else:
        print("Bye")