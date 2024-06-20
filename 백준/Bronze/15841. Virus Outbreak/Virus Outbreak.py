cows = [0, 1]
for i in range(2, 491):
    cows.append(cows[i-1]+cows[i-2])

while True:
    n = int(input())
    if n == -1:
        break
    print(f'Hour {n}: {cows[n]} cow(s) affected')