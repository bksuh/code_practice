for i in range(1, 101):
    for j in range(2, 101):
        for k in range(j+1, 101):
            for v in range(k+1, 101):
                if pow(i,3) == pow(j,3) + pow(k,3) + pow(v,3):
                    print(f"Cube = {i}, Triple = ({j},{k},{v})")