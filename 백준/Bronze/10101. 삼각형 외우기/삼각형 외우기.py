angles = [int(input()) for _ in range(3)]
if sum(angles) != 180:
    print("Error")
else:
    if angles.count(angles[0]) == 3:
        print("Equilateral")
    elif angles.count(angles[0]) == 2 or angles.count(angles[1]) == 2:
        print("Isosceles")
    else:
        print("Scalene")