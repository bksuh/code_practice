result = input()
arr = []
length = 0

for plate in result:
    if not arr:
        arr.append(plate)
        length += 10

    elif plate == arr[-1]:
        arr.append(plate)
        length += 5
    else:
        arr.append(plate)
        length += 10

print(length)