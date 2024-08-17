s = input()
target = "UCPC"
index = 0
    
for char in s:
    if char == target[index]:
        index += 1
        if index == 4:
            break
    
if index == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")