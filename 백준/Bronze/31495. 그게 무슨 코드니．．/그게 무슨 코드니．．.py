target = input()
if target[0] != '"' or target[-1] !='"' or len(target) < 3:
    print("CE")

else:
    print(target[1:-1])
